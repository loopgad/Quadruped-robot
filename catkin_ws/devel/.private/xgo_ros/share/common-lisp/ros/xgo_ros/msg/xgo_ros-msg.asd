
(cl:in-package :asdf)

(defsystem "xgo_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ArmPose" :depends-on ("_package_ArmPose"))
    (:file "_package_ArmPose" :depends-on ("_package"))
    (:file "BodyPose" :depends-on ("_package_BodyPose"))
    (:file "_package_BodyPose" :depends-on ("_package"))
    (:file "JointAngle" :depends-on ("_package_JointAngle"))
    (:file "_package_JointAngle" :depends-on ("_package"))
    (:file "LegPose" :depends-on ("_package_LegPose"))
    (:file "_package_LegPose" :depends-on ("_package"))
  ))