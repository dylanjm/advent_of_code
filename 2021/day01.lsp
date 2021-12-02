(defun get-input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
      while line
      collect line)))

(defparameter *input* (map 'list 'parse-integer (get-input "./inputs/input0101.txt")))

(scan-multiple 'list '(a b) *input*)
