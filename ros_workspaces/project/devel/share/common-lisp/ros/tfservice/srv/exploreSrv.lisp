; Auto-generated. Do not edit!


(cl:in-package tfservice-srv)


;//! \htmlinclude exploreSrv-request.msg.html

(cl:defclass <exploreSrv-request> (roslisp-msg-protocol:ros-message)
  ((zumy
    :reader zumy
    :initarg :zumy
    :type cl:string
    :initform "")
   (position
    :reader position
    :initarg :position
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (photo_data
    :reader photo_data
    :initarg :photo_data
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (finished
    :reader finished
    :initarg :finished
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass exploreSrv-request (<exploreSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <exploreSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'exploreSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tfservice-srv:<exploreSrv-request> is deprecated: use tfservice-srv:exploreSrv-request instead.")))

(cl:ensure-generic-function 'zumy-val :lambda-list '(m))
(cl:defmethod zumy-val ((m <exploreSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:zumy-val is deprecated.  Use tfservice-srv:zumy instead.")
  (zumy m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <exploreSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:position-val is deprecated.  Use tfservice-srv:position instead.")
  (position m))

(cl:ensure-generic-function 'photo_data-val :lambda-list '(m))
(cl:defmethod photo_data-val ((m <exploreSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:photo_data-val is deprecated.  Use tfservice-srv:photo_data instead.")
  (photo_data m))

(cl:ensure-generic-function 'finished-val :lambda-list '(m))
(cl:defmethod finished-val ((m <exploreSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:finished-val is deprecated.  Use tfservice-srv:finished instead.")
  (finished m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <exploreSrv-request>) ostream)
  "Serializes a message object of type '<exploreSrv-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'zumy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'zumy))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'position))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'position))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'photo_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'photo_data))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'finished) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <exploreSrv-request>) istream)
  "Deserializes a message object of type '<exploreSrv-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'zumy) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'zumy) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'position) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'position)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'photo_data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'photo_data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:setf (cl:slot-value msg 'finished) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<exploreSrv-request>)))
  "Returns string type for a service object of type '<exploreSrv-request>"
  "tfservice/exploreSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'exploreSrv-request)))
  "Returns string type for a service object of type 'exploreSrv-request"
  "tfservice/exploreSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<exploreSrv-request>)))
  "Returns md5sum for a message object of type '<exploreSrv-request>"
  "dfc249f6ae2c71d4941112c8c44769e2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'exploreSrv-request)))
  "Returns md5sum for a message object of type 'exploreSrv-request"
  "dfc249f6ae2c71d4941112c8c44769e2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<exploreSrv-request>)))
  "Returns full string definition for message of type '<exploreSrv-request>"
  (cl:format cl:nil "string zumy~%float32[] position~%float32[] photo_data~%bool finished~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'exploreSrv-request)))
  "Returns full string definition for message of type 'exploreSrv-request"
  (cl:format cl:nil "string zumy~%float32[] position~%float32[] photo_data~%bool finished~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <exploreSrv-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'zumy))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'photo_data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <exploreSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'exploreSrv-request
    (cl:cons ':zumy (zumy msg))
    (cl:cons ':position (position msg))
    (cl:cons ':photo_data (photo_data msg))
    (cl:cons ':finished (finished msg))
))
;//! \htmlinclude exploreSrv-response.msg.html

(cl:defclass <exploreSrv-response> (roslisp-msg-protocol:ros-message)
  ((position
    :reader position
    :initarg :position
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (hard_stop
    :reader hard_stop
    :initarg :hard_stop
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass exploreSrv-response (<exploreSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <exploreSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'exploreSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tfservice-srv:<exploreSrv-response> is deprecated: use tfservice-srv:exploreSrv-response instead.")))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <exploreSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:position-val is deprecated.  Use tfservice-srv:position instead.")
  (position m))

(cl:ensure-generic-function 'hard_stop-val :lambda-list '(m))
(cl:defmethod hard_stop-val ((m <exploreSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:hard_stop-val is deprecated.  Use tfservice-srv:hard_stop instead.")
  (hard_stop m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <exploreSrv-response>) ostream)
  "Serializes a message object of type '<exploreSrv-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'position))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'position))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'hard_stop) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <exploreSrv-response>) istream)
  "Deserializes a message object of type '<exploreSrv-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'position) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'position)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:setf (cl:slot-value msg 'hard_stop) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<exploreSrv-response>)))
  "Returns string type for a service object of type '<exploreSrv-response>"
  "tfservice/exploreSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'exploreSrv-response)))
  "Returns string type for a service object of type 'exploreSrv-response"
  "tfservice/exploreSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<exploreSrv-response>)))
  "Returns md5sum for a message object of type '<exploreSrv-response>"
  "dfc249f6ae2c71d4941112c8c44769e2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'exploreSrv-response)))
  "Returns md5sum for a message object of type 'exploreSrv-response"
  "dfc249f6ae2c71d4941112c8c44769e2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<exploreSrv-response>)))
  "Returns full string definition for message of type '<exploreSrv-response>"
  (cl:format cl:nil "float32[] position~%bool hard_stop~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'exploreSrv-response)))
  "Returns full string definition for message of type 'exploreSrv-response"
  (cl:format cl:nil "float32[] position~%bool hard_stop~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <exploreSrv-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <exploreSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'exploreSrv-response
    (cl:cons ':position (position msg))
    (cl:cons ':hard_stop (hard_stop msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'exploreSrv)))
  'exploreSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'exploreSrv)))
  'exploreSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'exploreSrv)))
  "Returns string type for a service object of type '<exploreSrv>"
  "tfservice/exploreSrv")