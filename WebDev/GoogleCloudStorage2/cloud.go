package main
import(
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"strings"
	"google.golang.org/cloud/storage"
	"net/http"
	"golang.org/x/net/context"
)
var bucket = "essys-bucket"

type demo struct {
	//Current Bucket
	bucket *storage.BucketHandle
	//Current Client
	client *storage.Client

	//Our writer, this is an http.ResponseWriter, but because we are pulling files it may be best to use a file-based writer instead.
	w   http.ResponseWriter
	//Current Context
	ctx context.Context
	// cleanUp is a list of filenames that need cleaning up at the end of the demo.
	cleanUp []string
	
	//just a placeholder I placed in the object so I could make sure everything was imported correctly before I started.
	placeholder string
	
	// failed indicates that one or more of the demo steps failed.
	failed bool
}

// createFile creates a file in Google Cloud Storage.
func (d *demo) createFile(fileName string) {
		//Prints to the webpage that the file is being created in a bucket with a filename.
        fmt.Fprintf(d.w, "Creating file /%v/%v\n", bucket, fileName)
		//Appears to be a writer for google cloud.
        wc := d.bucket.Object(fileName).NewWriter(d.ctx)
		//Data
        wc.ContentType = "text/plain"
		//More Data
        wc.Metadata = map[string]string{
                "x-goog-meta-foo": "foo",
                "x-goog-meta-bar": "bar",
        }
		//Need to look up what this does.
        d.cleanUp = append(d.cleanUp, fileName)
		//Writing to the writer abcde\n
        wc.Write([]byte("abcde\n"))
		//Writing to the writer a lot of f and then a newlone.
        wc.Write([]byte(strings.Repeat("f", 1024*4) + "\n"))
		//Closes the writer.
        wc.Close()
}




// readFile reads the named file in Google Cloud Storage.
func (d *demo) readFile(fileName string) {
		//Prints to webpage.
        io.WriteString(d.w, "\nAbbreviated file content (first line and last 1K):\n")
		//Make a reader for the google cloud.
        rc, _ := d.bucket.Object(fileName).NewReader(d.ctx)
		//Prepares the reader to close when readFile is done.
        defer rc.Close()
		//Reads the contents of the reader (the file contents) and stores them in slurp.
        slurp, _ := ioutil.ReadAll(rc)
		//Splits slurp on newline?
        fmt.Fprintf(d.w, "%s\n", bytes.SplitN(slurp, []byte("\n"), 2)[0])
		//If slurp is too large it will print some ... and then cut off 1024 of it's values.
		//Otherwise it will just print the whole thing.
        if len(slurp) > 1024 { fmt.Fprintf(d.w, "...%s\n", slurp[len(slurp)-1024:]) } else { fmt.Fprintf(d.w, "%s\n", slurp) }
}


func (d *demo) listBucket() {
	//Print to writer.
	io.WriteString(d.w, "\nListbucket result:\n")
	// Construct bucket query truncating up to "/"
	query := &storage.Query{Delimiter: "/"}
	// Get objects found by query.
	objs, _ := d.bucket.List(d.ctx, query)
	// For each object...
	for _, obj := range objs.Results {
		// Print its name.
		fmt.Fprintf(d.w,"\n" + obj.Name)
	}
	// For each prefix found
	for _, i := range objs.Prefixes{
		// Print the prefix.
		fmt.Fprintf(d.w,"\n" + i)
	}
}