;; Auto-generated. Do not edit!


(when (boundp 'assignments::RiskEvaluation)
  (if (not (find-package "ASSIGNMENTS"))
    (make-package "ASSIGNMENTS"))
  (shadow 'RiskEvaluation (find-package "ASSIGNMENTS")))
(unless (find-package "ASSIGNMENTS::RISKEVALUATION")
  (make-package "ASSIGNMENTS::RISKEVALUATION"))
(unless (find-package "ASSIGNMENTS::RISKEVALUATIONREQUEST")
  (make-package "ASSIGNMENTS::RISKEVALUATIONREQUEST"))
(unless (find-package "ASSIGNMENTS::RISKEVALUATIONRESPONSE")
  (make-package "ASSIGNMENTS::RISKEVALUATIONRESPONSE"))

(in-package "ROS")





(defclass assignments::RiskEvaluationRequest
  :super ros::object
  :slots (_x _y _z _hazard_type ))

(defmethod assignments::RiskEvaluationRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:hazard_type __hazard_type) "")
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _hazard_type (string __hazard_type))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:hazard_type
   (&optional __hazard_type)
   (if __hazard_type (setq _hazard_type __hazard_type)) _hazard_type)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; string _hazard_type
    4 (length _hazard_type)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _hazard_type
       (write-long (length _hazard_type) s) (princ _hazard_type s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _hazard_type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _hazard_type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass assignments::RiskEvaluationResponse
  :super ros::object
  :slots (_success _message ))

(defmethod assignments::RiskEvaluationResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass assignments::RiskEvaluation
  :super ros::object
  :slots ())

(setf (get assignments::RiskEvaluation :md5sum-) "2ad8d9fb9c81a63740c12dbd83c357d9")
(setf (get assignments::RiskEvaluation :datatype-) "assignments/RiskEvaluation")
(setf (get assignments::RiskEvaluation :request) assignments::RiskEvaluationRequest)
(setf (get assignments::RiskEvaluation :response) assignments::RiskEvaluationResponse)

(defmethod assignments::RiskEvaluationRequest
  (:response () (instance assignments::RiskEvaluationResponse :init)))

(setf (get assignments::RiskEvaluationRequest :md5sum-) "2ad8d9fb9c81a63740c12dbd83c357d9")
(setf (get assignments::RiskEvaluationRequest :datatype-) "assignments/RiskEvaluationRequest")
(setf (get assignments::RiskEvaluationRequest :definition-)
      "# RiskEvaluation.srv
float64 x
float64 y
float64 z
string hazard_type   # E.g., \"High\", \"Medium\", \"Low\" 

---
bool success
string message  # Additional message, e.g., \"Moving to a safer distance.\"
")

(setf (get assignments::RiskEvaluationResponse :md5sum-) "2ad8d9fb9c81a63740c12dbd83c357d9")
(setf (get assignments::RiskEvaluationResponse :datatype-) "assignments/RiskEvaluationResponse")
(setf (get assignments::RiskEvaluationResponse :definition-)
      "# RiskEvaluation.srv
float64 x
float64 y
float64 z
string hazard_type   # E.g., \"High\", \"Medium\", \"Low\" 

---
bool success
string message  # Additional message, e.g., \"Moving to a safer distance.\"
")



(provide :assignments/RiskEvaluation "2ad8d9fb9c81a63740c12dbd83c357d9")


