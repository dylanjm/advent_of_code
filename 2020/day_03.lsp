(defun get-input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
      while line
      collect line)))

(defparameter *input* (get-input "./inputs/input03.txt"))
