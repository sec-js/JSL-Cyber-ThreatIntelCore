#TOR Exit Nodes

## Summary
This DataSet provides information for identifying TOR Exit Nodes by preprogramed Tags/Variables. The primary function for the outputted data is aimed at providing a highly granular Exit node Profiler for, but not limited to “Black Listing” and “Threat Intelligence “initiatives. Tor relays are also referred to as "routers" or "nodes”. They receive traffic on the Tor network and pass it along. An “exit relay” is the final relay that Tor traffic passes through before it reaches its destination. Exit relays advertise their presence to the entire Tor network, so any Tor users can use them. Because Tor traffic exits through these relays, the IP address of the exit relay is interpreted as the source of the traffic. 

## Description
The Data shown in this OutPut is aggregated from various Source URLS that provided very basic information on these Exit Node Addresses. The DataSet Schema was expanded by using, “WhoIs” and “FingerPrint” data on ExitNode addresses. By scraping this data and performing these additional searching queries, we were able to optimize the amount of information to profile these Exit Nodes.


## Facts
- Date Created: 2016-01-18
- Date Modified: 2016-03-06
- Version: 2016.1
- Update Frequency: 72 hours
- Temporal Coverage: 2016-03 to 2016-04
- Spatial Coverage: Global
- Sources: TOR Exit Nodes and TOR Exit Relay
- Source URL: -
- Source License Requirements: None
- Source Citation: TOR_IP_RESOLUTION_OUTPUT.csv
- Keywords:
  - TOR Relay
  - TOR Exit Nodes
  - TOR Routers
- Other Titles and Uses:
  - Cyber - TOR Exit Nodes
  - Cyber  - TOR Exit Relays
  - Cyber – TOR Exit IPs


## Schema
- Data_Upload_ID_Text
  - Type: String

- Universally_Unique_Identifier_Text
  - A universally unique identifier (UUID) is an identifier standard used in software construction. A UUID consists of a 128-bit value. A UUID is formatted according to a specified variant and a specific version of the variant, and the meaning of each bit is defined by any of several variants.
  - Type: String

- Referential_Text
  - Type: String

- Data_Source_Name
  - This is always "jsl"
  - Type: String

- Date
  - Date of first uptime?
  - Type: Date 

- Cog

- Model

- Concept

- Segment

- Pedigree_Number
  - Quality/integrity of data source
  - Type: Number

- Confidence_Score_Number
  - Number between 1 and 10 which defines the reliability of the data
  - Type: Integer
  - Required

- IP_Address_Text
  - IP address corresponding to entry on blacklist
  - Type: String
  - Required

- IP_Address_Integer
  - IP address represented in integer notation. An IP address in string form can be converted to integer form by breaking it into four octets. We then perform a calculation on these. For example, given the IP address 213.122.92.232, we have:
    - First Octet:  213
    - Second Octet: 122
    - Third Octet:  92
    - Fourth Octet: 232

  And then we can perform the calculation as follows:

  (first octet * 256³) + (second octet * 256²) + (third octet * 256) + (fourth octet)

  = (first octet * 16777216) + (second octet * 65536) + (third octet * 256) + (fourth octet)

  = (213 * 16777216) + (122 * 65536) + (92 * 256) + (232)
  
  = 3581566184.
  - Type: Integer
  - Required

- Offender_Class_Text
  - The offender class determines the type of blacklist. The offender class for this dataset is "dns_bl".
  - Type: String
  - Required

- First_Observed_date
  - Date corresponding to the first time the item was observed.
  - Type: Date
  - Required

- First_Observed_time
  - Time corresponding to the first time the item was observed
  - Type: Time
  - Required

- Most_Recent_Observation_date
  - Date corresponding to most recent observation of entry.
  - Type: Date
  - Required

- Most_Recent_Observation_time
  - Time corresponding to most recent observation of entry.
  - Type: Time
  - Required

- Total_Observations_Integer
  - Total number of times entry has been observed.
  - Type: Integer
  - Required

- Blacklist_Ranking_Integer
  - Ranking correspinding to blacklist/item in blacklist. 
  - Type: Integer

- Threat_Score_Integer
  - Type: Integer

- Total_Capabilities_Integer
  - Type: Integer

- Commvett 

- Commdatevett

- Govvett

- Govdatevett

- Country_Abbreviation_Text
  - Two letter country code.
  - Type: String

- Country_Text
  - Country corresponding to listed item.
  - Type: String

- City_Name
  - City corresponding to location of IP address/domain of blacklist entry.
  - Type: String

- Coordinates_Number
  - Coordinates corresponding to loaction of IP address/domain od blacklist entry.
  - Type: Location
  - Format: GeoPoint

- Geographic_Longitude
  - Geographic longitude corresponding to location of IP address/domain on entry.
  - Type: Location

- Geographic_Latitude
  - Geographic latitude corresponding to location of IP address/domain on entry.
  - Type: Location

- ISP_Text
  - An Internet service provider (ISP) is an organization that provides services for accessing and using the Internet. Internet services typically provided by ISPs, include Internet access, Internet transit, domain name registration, web hosting, Usenet service, and colocation. They may be commercial, community-owned, non-profit, or otherwise privately owned. Classifications include the following:
  
    - Access providers ISP
    - Edge providers
    - Mailbox providers
    - Hosting ISPs
    - Transit ISPs
    - Virtual ISPs
    - Free ISPs
    - Wireless ISP
  - Type: String

- Domain_Name
  - Domain name of an entry in the blacklist.
  - Type: String

- Network_Speed_Number
  - Network speed corresponding to entry in dataset.
  - Type: Number

- Network_Autonomous_System_Number
  - An autonomous system number (ASN) is a unique number that's available globally to identify an autonomous system and which enables that system to exchange exterior routing information with other neighboring autonomous systems. 
  The number of autonomous system numbers is limited. For autonomous system numbers to be assigned, current guidelines need the network to be multi-homed and have a unique routing policy. Autonomous system numbers can be assigned only through a request to the local Internet registry.
  - Type: Integer

- Network_Class
  - This could be one of five IP network classes: A, B, C, D or E. Network addressing architecture divides the address space into these five classes. Each class defines either a network size for the number of hosts for unicast addresses (classes A, B, C), or a multicast network (class D). The fifth class (E) is reserved for future or experimental purposes.

    - Class A: Class A addresses are IP addresses that are assigned to network devices, such as computers, and include all addresses in which the first bit of the first octet is set to 0 (zero). This includes all values from 00000001 to 01111111, or 1 to 127.

    - Class B: Class B addresses are IP addresses that are assigned to network devices, such as computers, and include all addresses in which the first two bits of the first octet are 10. This includes all values from 10000000 to 10111111, or 128 to 191.
    

    - Class C: Class C addresses are IP addresses that are assigned to network devices, such as computers, and include all addresses in which the first three bits of the first octet are set to 110. This includes all values from 11000000 to 11011111, or 192 to 223.

    - Class D: Class D network addresses are not assigned to devices on a network. These addresses are used for special-purpose, multicast applications (such as video- and audio-streaming applications). These addresses all need to be registered with IANA to be used globally. Addresses in this class have the first bits of the first octet set to 1110, yielding addresses in the first octet ranging from 11100000 to 11101111, or 224 to 239. These addresses are not defined by a normal subnet mask; instead, each address is used for a specific purpose. And because each address is individually used, it uses a 255.255.255.255 mask.

    - Class E: If Class D is special, Class E addresses are even more special. There is no defined use for this address class. Officially, it is listed as reserved for usage and testing by IANA and the Internet Research Task Force (IRTF). In fact, as of RFC3330 in 2002, Class E was updated to “reserved for future use.” Class E comprises absolutely all valid addresses with 240 or higher in the first octet. The first bits of the first octet is 1111, which yields addresses from 11110000 to 11111110 — or technically, 11111111 — which, in decimals, are 240 to 254 — or 255.
  - Type: String

- Network_Type_Text
  - This could be one of the following types: LAN, WAN, WLAN, MAN, SAN, PAN, EPN or VPN. 
  The "network type" defines the type of computer network involved,and it can characterise the size as well as the purpose of the network. The size of a network can be expressed by the geographic area it occupies and the number of computers    which form the network. It could comprise of a few devices occupying a single room, or millions of devices spread across  the entire globe. Examples of networks based on size are:
    - Personal area network, or PAN
    - Local area network, or LAN
    - Metropolitan area network, or MAN
    - Wide area network, or WAN

    In terms of purpose, many networks can be considered general purpose, which means they are used for everything from sending files to a printer to accessing the Internet. Some types of networks, however, serve a very particular purpose.Some of the different networks based on their main purpose are:
    - Storage area network, or SAN
    - Enterprise private network, or EPN
    - Virtual private network, or VPN
    
  - Type: String

- is_Active
  - Determines whether IP/domain in list is active or not.
  - Type: Boolean

- Insrtdttm

- Updtdttm