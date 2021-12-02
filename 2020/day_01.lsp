(ql:quickload :alexandria)

(defun get-input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
      while line
      collect line)))

(defparameter *input* (map 'list 'parse-integer (get-input "./inputs/input011.txt")))

;;; Part 1
(let* ( (diff    (map 'list #'(lambda (x) (- 2020 x)) *input*))
        (matches (loop for num in diff
                   when (car (member num *input*))
                   collect it)))
  (assert (= 2020 (apply '+ matches)))
  (apply '* matches))

;;; Part 2
(defun find-trip (i)
  (labels ((rec (input)
             (let* ( (first           (car input))
                     (diffs           (loop for num in (cdr input)
                                        for x = (+ first num)
                                        when (< x 2020)
                                        collect (list first num x)))
                     (possible-thirds (loop for group in diffs
                                        for diff = (- 2020 (car (last group)))
                                        for mem = (car (member diff input))
                                        when mem
                                        collect (list (car group) (cadr group) mem))))
               (if possible-thirds
                 (apply '* (car possible-thirds))
                 (rec (cdr input))))))
    (rec i)))

(find-trip *input*)
