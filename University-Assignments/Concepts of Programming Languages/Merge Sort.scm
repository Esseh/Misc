;Kenneth Willeford
;CSCI 117
;Merge Sort Implementation in Scheme / Practice for Functional Programming
;
; This program contains an implementation of merge sort in scheme, there's
; not much more to be said that isn't in the function documentation.
;
; 


;Aliases for car/cdr because I am used to Haskell Syntax.
(define head car)
(define tail cdr)

;Split is a recursive function that separates a list into two without regard for its order.(Order is not necessary for Merge Sort)
;The Algorithm works like so...
(define split 
    (lambda (lst left right)
        (cond
            [(null? lst) (cond ;If the input list is NULL then return the relevant lists.
							[(null? left)(list right)]
							[(null? right)(list left)]
							[else (list left right)]
						)
			]
            [(eq? (length lst) 1) (split ;If the remaining list size is only 1 then just place on the left list.
                                    (tail lst)
                                    (cons (head lst) left)
                                    right
                                   )
            ]
            [else (split 				;Otherwise move the first element to the left list and the second element to the right list.
                        (tail (tail lst))
                        (cons (head lst) left)
                        (cons (head (tail lst)) right)
                    )
            ]
        )
    )
)
; Thus a list such as 1,2,3,4,5 null null
; Will produce the following output
; [3,4,5] [1] [2]
; [5] [3,1] [4,2]
; [5,3,1] [4,2]


;The Merge Function takes two lists and puts them together in sorted order.
;One thing to note is that appending to a list is expensive in Scheme, as such some time 
;is saved by putting it together backwards and then reversing the output.
(define merge 
	(lambda (lst1 lst2 output)
        (cond
            [(and (null? lst1) (null? lst2)) (reverse output)] ;If both lists are empty then reverse the output so that it is in the correct order.
			[(null? lst1) (merge							   ;If the first list is empty, then just prepend the next item of the second list.
								'()
								(tail lst2)
								(cons (head lst2) output)
							)]
			[(null? lst2) (merge							   ;If the second list is empty, then just prepend the next item of the first list.
								(tail lst1)
								'()
								(cons (head lst1) output)
							)]
            [else (cond 												;If both lists exist then make a comparison between each of the first elements.
                        [(< (head lst1) (head lst2)) (merge				;If the first list's head value is smaller then prepend it.
															(tail lst1)
															lst2
															(cons (head lst1) output)
														)
						]
						[else (merge									;Otherwise prepend the second list's head value.
									lst1
									(tail lst2)
									(cons (head lst2) output)
								)
						]
                    )
            ]
        )
	)
)

;Merge Sort Works by dividing and conquering..
;The lists have to be divided into two until they are lists of only one element. 
;At which point they are stitched back together in the correct order. 
;To do this I have two helper function split and merge, refer to their documentation for details.
(define mergeSort 
	(lambda (lst)
        (cond
			[(null? lst) '()]				;An Empty List is Sorted	(Base Case 1)
			[(eq? 1 (length lst)) lst]		;A list of 1 is Sorted		(Base Case 2)
			[else 
				(let ((x (split lst '() '())))	;Create a temporary value holding the list split in two.
					(merge						; Merge together....
						(mergeSort (head x))		;Each List...
						(mergeSort (head (tail x))) ;Being recursive splitted and merged.... until a base case is reached.
						'()
					)
				)
			]
        )
	)
)

;The Main Function , Runs and print out I/O
(begin
		(display (mergeSort (list 18 3 3 92 5)))
		(newline)
		(display (mergeSort '()))
		(newline)
		(display (mergeSort (list 1 2 3 4 5)))
		(newline)
		(display (mergeSort (list 5 4 3 2 1)))
		(newline)
)



;OUTPUT

Share Link:

https://repl.it/B5Uw/20
Share on: