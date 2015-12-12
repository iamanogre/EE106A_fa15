// Generated by gencpp from file tfservice/exploreSrv.msg
// DO NOT EDIT!


#ifndef TFSERVICE_MESSAGE_EXPLORESRV_H
#define TFSERVICE_MESSAGE_EXPLORESRV_H

#include <ros/service_traits.h>


#include <tfservice/exploreSrvRequest.h>
#include <tfservice/exploreSrvResponse.h>


namespace tfservice
{

struct exploreSrv
{

typedef exploreSrvRequest Request;
typedef exploreSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct exploreSrv
} // namespace tfservice


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::tfservice::exploreSrv > {
  static const char* value()
  {
    return "dfc249f6ae2c71d4941112c8c44769e2";
  }

  static const char* value(const ::tfservice::exploreSrv&) { return value(); }
};

template<>
struct DataType< ::tfservice::exploreSrv > {
  static const char* value()
  {
    return "tfservice/exploreSrv";
  }

  static const char* value(const ::tfservice::exploreSrv&) { return value(); }
};


// service_traits::MD5Sum< ::tfservice::exploreSrvRequest> should match 
// service_traits::MD5Sum< ::tfservice::exploreSrv > 
template<>
struct MD5Sum< ::tfservice::exploreSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::tfservice::exploreSrv >::value();
  }
  static const char* value(const ::tfservice::exploreSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::tfservice::exploreSrvRequest> should match 
// service_traits::DataType< ::tfservice::exploreSrv > 
template<>
struct DataType< ::tfservice::exploreSrvRequest>
{
  static const char* value()
  {
    return DataType< ::tfservice::exploreSrv >::value();
  }
  static const char* value(const ::tfservice::exploreSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::tfservice::exploreSrvResponse> should match 
// service_traits::MD5Sum< ::tfservice::exploreSrv > 
template<>
struct MD5Sum< ::tfservice::exploreSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::tfservice::exploreSrv >::value();
  }
  static const char* value(const ::tfservice::exploreSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::tfservice::exploreSrvResponse> should match 
// service_traits::DataType< ::tfservice::exploreSrv > 
template<>
struct DataType< ::tfservice::exploreSrvResponse>
{
  static const char* value()
  {
    return DataType< ::tfservice::exploreSrv >::value();
  }
  static const char* value(const ::tfservice::exploreSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TFSERVICE_MESSAGE_EXPLORESRV_H
