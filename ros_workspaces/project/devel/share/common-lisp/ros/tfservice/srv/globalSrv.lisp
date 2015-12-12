; Auto-generated. Do not edit!


(cl:in-package tfservice-srv)


;//! \htmlinclude globalSrv-request.msg.html

(cl:defclass <globalSrv-request> (roslisp-msg-protocol:ros-message)
  ((zumy
    :reader zumy
    :initarg :zumy
    :type cl:string
    :initform ""))
)

(cl:defclass globalSrv-request (<globalSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <globalSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'globalSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tfservice-srv:<globalSrv-request> is deprecated: use tfservice-srv:globalSrv-request instead.")))

(cl:ensure-generic-function 'zumy-val :lambda-list '(m))
(cl:defmethod zumy-val ((m <globalSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:zumy-val is deprecated.  Use tfservice-srv:zumy instead.")
  (zumy m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <globalSrv-request>) ostream)
  "Serializes a message object of type '<globalSrv-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'zumy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'zumy))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <globalSrv-request>) istream)
  "Deserializes a message object of type '<globalSrv-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'zumy) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'zumy) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<globalSrv-request>)))
  "Returns string type for a service object of type '<globalSrv-request>"
  "tfservice/globalSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'globalSrv-request)))
  "Returns string type for a service object of type 'globalSrv-request"
  "tfservice/globalSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<globalSrv-request>)))
  "Returns md5sum for a message object of type '<globalSrv-request>"
  "fe3632406195713ff0da2cbdf8e828bf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'globalSrv-request)))
  "Returns md5sum for a message object of type 'globalSrv-request"
  "fe3632406195713ff0da2cbdf8e828bf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<globalSrv-request>)))
  "Returns full string definition for message of type '<globalSrv-request>"
  (cl:format cl:nil "string zumy~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'globalSrv-request)))
  "Returns full string definition for message of type 'globalSrv-request"
  (cl:format cl:nil "string zumy~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <globalSrv-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'zumy))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <globalSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'globalSrv-request
    (cl:cons ':zumy (zumy msg))
))
;//! \htmlinclude globalSrv-response.msg.html

(cl:defclass <globalSrv-response> (roslisp-msg-protocol:ros-message)
  ((updated
    :reader updated
    :initarg :updated
    :type cl:boolean
    :initform cl:nil)
   (theta
    :reader theta
    :initarg :theta
    :type cl:float
    :initform 0.0)
   (position
    :reader position
    :initarg :position
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass globalSrv-response (<globalSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <globalSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'globalSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tfservice-srv:<globalSrv-response> is deprecated: use tfservice-srv:globalSrv-response instead.")))

(cl:ensure-generic-function 'updated-val :lambda-list '(m))
(cl:defmethod updated-val ((m <globalSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:updated-val is deprecated.  Use tfservice-srv:updated instead.")
  (updated m))

(cl:ensure-generic-function 'theta-val :lambda-list '(m))
(cl:defmethod theta-val ((m <globalSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:theta-val is deprecated.  Use tfservice-srv:theta instead.")
  (theta m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <globalSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tfservice-srv:position-val is deprecated.  Use tfservice-srv:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <globalSrv-response>) ostream)
  "Serializes a message object of type '<globalSrv-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'updated) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
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
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <globalSrv-response>) istream)
  "Deserializes a message object of type '<globalSrv-response>"
    (cl:setf (cl:slot-value msg 'updated) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta) (roslisp-utils:decode-single-float-bits bits)))
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<globalSrv-response>)))
  "Returns string type for a service object of type '<globalSrv-response>"
  "tfservice/globalSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'globalSrv-response)))
  "Returns string type for a service object of type 'globalSrv-response"
  "tfservice/globalSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<globalSrv-response>)))
  "Returns md5sum for a message object of type '<globalSrv-response>"
  "fe3632406195713ff0da2cbdf8e828bf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'globalSrv-response)))
  "Returns md5sum for a message object of type 'globalSrv-response"
  "fe3632406195713ff0da2cbdf8e828bf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<globalSrv-response>)))
  "Returns full string definition for message of type '<globalSrv-response>"
  (cl:format cl:nil "bool updated~%float32 theta~%float32[] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'globalSrv-response)))
  "Returns full string definition for message of type 'globalSrv-response"
  (cl:format cl:nil "bool updated~%float32 theta~%float32[] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <globalSrv-response>))
  (cl:+ 0
     1
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <globalSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'globalSrv-response
    (cl:cons ':updated (updated msg))
    (cl:cons ':theta (theta msg))
    (cl:cons ':position (position msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'globalSrv)))
  'globalSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'globalSrv)))
  'globalSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'globalSrv)))
  "Returns string type for a service object of type '<globalSrv>"
  "tfservice/globalSrv")