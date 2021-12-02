(defun get-input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
      while line
      for info = (uiop:split-string line)
      for char = (coerce (remove #\: (cadr info)) 'character)
      for pos = (map 'cons #'parse-integer
                  (uiop:split-string
                    (car info) :separator '(#\-)))
      collect (list pos char (caddr info)))))

(defparameter *input* (get-input "./inputs/input02.txt"))

(defun between-p (lower upper actual)
  (and (>= actual lower) (<= actual upper)))

(defun valid-password? (input)
  (let* ( (char-of-interest (cadr input))
          (num-char-oi      (length
                              (remove char-of-interest
                                (caddr input) :test #'char-not-equal))))
    (between-p (caar input) (cadar input) num-char-oi)))

(loop for input in *input*
  counting (valid-password? input) into total
  finally (return total))

(defun valid-password-pt2? (input)
  (let* ( (char-of-interest (cadr input))
          (password         (caddr input))
          (pos              (map 'list #'1- (car input)))
          (correct?         (map 'list
                              #'(lambda (x) (char-equal (elt password x) char-of-interest)) pos)))
    (cond
      ((and (car correct?) (cadr correct?)) nil)
      ((or (car correct?) (cadr correct?)) t))))

(loop for input in *input*
  counting (valid-password-pt2? input) into total
  finally (return total))
