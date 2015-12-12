// Generated by gencpp from file tfservice/exploreSrvRequest.msg
// DO NOT EDIT!


#ifndef TFSERVICE_MESSAGE_EXPLORESRVREQUEST_H
#define TFSERVICE_MESSAGE_EXPLORESRVREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace tfservice
{
template <class ContainerAllocator>
struct exploreSrvRequest_
{
  typedef exploreSrvRequest_<ContainerAllocator> Type;

  exploreSrvRequest_()
    : zumy()
    , position()
    , photo_data()
    , finished(false)  {
    }
  exploreSrvRequest_(const ContainerAllocator& _alloc)
    : zumy(_alloc)
    , position(_alloc)
    , photo_data(_alloc)
    , finished(false)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _zumy_type;
  _zumy_type zumy;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _position_type;
  _position_type position;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _photo_data_type;
  _photo_data_type photo_data;

   typedef uint8_t _finished_type;
  _finished_type finished;




  typedef boost::shared_ptr< ::tfservice::exploreSrvRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tfservice::exploreSrvRequest_<ContainerAllocator> const> ConstPtr;

}; // struct exploreSrvRequest_

typedef ::tfservice::exploreSrvRequest_<std::allocator<void> > exploreSrvRequest;

typedef boost::shared_ptr< ::tfservice::exploreSrvRequest > exploreSrvRequestPtr;
typedef boost::shared_ptr< ::tfservice::exploreSrvRequest const> exploreSrvRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tfservice::exploreSrvRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tfservice::exploreSrvRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace tfservice

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'tf2_msgs': ['/opt/ros/indigo/share/tf2_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tfservice::exploreSrvRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tfservice::exploreSrvRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tfservice::exploreSrvRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "56ed2e40a7e2814fecf7cc40556f9ead";
  }

  static const char* value(const ::tfservice::exploreSrvRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x56ed2e40a7e2814fULL;
  static const uint64_t static_value2 = 0xecf7cc40556f9eadULL;
};

template<class ContainerAllocator>
struct DataType< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tfservice/exploreSrvRequest";
  }

  static const char* value(const ::tfservice::exploreSrvRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string zumy\n\
float32[] position\n\
float32[] photo_data\n\
bool finished\n\
";
  }

  static const char* value(const ::tfservice::exploreSrvRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.zumy);
      stream.next(m.position);
      stream.next(m.photo_data);
      stream.next(m.finished);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct exploreSrvRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tfservice::exploreSrvRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tfservice::exploreSrvRequest_<ContainerAllocator>& v)
  {
    s << indent << "zumy: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.zumy);
    s << indent << "position[]" << std::endl;
    for (size_t i = 0; i < v.position.size(); ++i)
    {
      s << indent << "  position[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.position[i]);
    }
    s << indent << "photo_data[]" << std::endl;
    for (size_t i = 0; i < v.photo_data.size(); ++i)
    {
      s << indent << "  photo_data[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.photo_data[i]);
    }
    s << indent << "finished: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.finished);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TFSERVICE_MESSAGE_EXPLORESRVREQUEST_H