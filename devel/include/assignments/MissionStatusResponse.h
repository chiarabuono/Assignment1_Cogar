// Generated by gencpp from file assignments/MissionStatusResponse.msg
// DO NOT EDIT!


#ifndef ASSIGNMENTS_MESSAGE_MISSIONSTATUSRESPONSE_H
#define ASSIGNMENTS_MESSAGE_MISSIONSTATUSRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace assignments
{
template <class ContainerAllocator>
struct MissionStatusResponse_
{
  typedef MissionStatusResponse_<ContainerAllocator> Type;

  MissionStatusResponse_()
    : mission_complete(false)
    , message()  {
    }
  MissionStatusResponse_(const ContainerAllocator& _alloc)
    : mission_complete(false)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _mission_complete_type;
  _mission_complete_type mission_complete;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _message_type;
  _message_type message;





  typedef boost::shared_ptr< ::assignments::MissionStatusResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::assignments::MissionStatusResponse_<ContainerAllocator> const> ConstPtr;

}; // struct MissionStatusResponse_

typedef ::assignments::MissionStatusResponse_<std::allocator<void> > MissionStatusResponse;

typedef boost::shared_ptr< ::assignments::MissionStatusResponse > MissionStatusResponsePtr;
typedef boost::shared_ptr< ::assignments::MissionStatusResponse const> MissionStatusResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::assignments::MissionStatusResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::assignments::MissionStatusResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::assignments::MissionStatusResponse_<ContainerAllocator1> & lhs, const ::assignments::MissionStatusResponse_<ContainerAllocator2> & rhs)
{
  return lhs.mission_complete == rhs.mission_complete &&
    lhs.message == rhs.message;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::assignments::MissionStatusResponse_<ContainerAllocator1> & lhs, const ::assignments::MissionStatusResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace assignments

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::assignments::MissionStatusResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::assignments::MissionStatusResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::assignments::MissionStatusResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::assignments::MissionStatusResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::assignments::MissionStatusResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::assignments::MissionStatusResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::assignments::MissionStatusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a6469b1a790f365f804bd4f1a739016d";
  }

  static const char* value(const ::assignments::MissionStatusResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa6469b1a790f365fULL;
  static const uint64_t static_value2 = 0x804bd4f1a739016dULL;
};

template<class ContainerAllocator>
struct DataType< ::assignments::MissionStatusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "assignments/MissionStatusResponse";
  }

  static const char* value(const ::assignments::MissionStatusResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::assignments::MissionStatusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Response: Confirmation of mission status.\n"
"bool mission_complete  # Whether the mission is completed successfully.\n"
"string message  # Additional message about the mission, e.g., \"Mission completed successfully.\"\n"
;
  }

  static const char* value(const ::assignments::MissionStatusResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::assignments::MissionStatusResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.mission_complete);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MissionStatusResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::assignments::MissionStatusResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::assignments::MissionStatusResponse_<ContainerAllocator>& v)
  {
    s << indent << "mission_complete: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.mission_complete);
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ASSIGNMENTS_MESSAGE_MISSIONSTATUSRESPONSE_H
