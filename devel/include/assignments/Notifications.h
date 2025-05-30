// Generated by gencpp from file assignments/Notifications.msg
// DO NOT EDIT!


#ifndef ASSIGNMENTS_MESSAGE_NOTIFICATIONS_H
#define ASSIGNMENTS_MESSAGE_NOTIFICATIONS_H

#include <ros/service_traits.h>


#include <assignments/NotificationsRequest.h>
#include <assignments/NotificationsResponse.h>


namespace assignments
{

struct Notifications
{

typedef NotificationsRequest Request;
typedef NotificationsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Notifications
} // namespace assignments


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::assignments::Notifications > {
  static const char* value()
  {
    return "31471cbc5866c6110d0f43de5ac7621e";
  }

  static const char* value(const ::assignments::Notifications&) { return value(); }
};

template<>
struct DataType< ::assignments::Notifications > {
  static const char* value()
  {
    return "assignments/Notifications";
  }

  static const char* value(const ::assignments::Notifications&) { return value(); }
};


// service_traits::MD5Sum< ::assignments::NotificationsRequest> should match
// service_traits::MD5Sum< ::assignments::Notifications >
template<>
struct MD5Sum< ::assignments::NotificationsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::assignments::Notifications >::value();
  }
  static const char* value(const ::assignments::NotificationsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::assignments::NotificationsRequest> should match
// service_traits::DataType< ::assignments::Notifications >
template<>
struct DataType< ::assignments::NotificationsRequest>
{
  static const char* value()
  {
    return DataType< ::assignments::Notifications >::value();
  }
  static const char* value(const ::assignments::NotificationsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::assignments::NotificationsResponse> should match
// service_traits::MD5Sum< ::assignments::Notifications >
template<>
struct MD5Sum< ::assignments::NotificationsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::assignments::Notifications >::value();
  }
  static const char* value(const ::assignments::NotificationsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::assignments::NotificationsResponse> should match
// service_traits::DataType< ::assignments::Notifications >
template<>
struct DataType< ::assignments::NotificationsResponse>
{
  static const char* value()
  {
    return DataType< ::assignments::Notifications >::value();
  }
  static const char* value(const ::assignments::NotificationsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ASSIGNMENTS_MESSAGE_NOTIFICATIONS_H
