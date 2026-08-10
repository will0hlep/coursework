//lesson 1
typedef enum {
  INTEGER,
  STRING,
} snek_object_kind_t;

// don't touch below this line'

typedef union SnekObjectData {
  int v_int;
  char *v_string;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t new_integer(int);
snek_object_t new_string(char *str);
void format_object(snek_object_t obj, char *buffer);

//lesson 5
#include <stdint.h>

typedef struct tcp_header {
  uint16_t src_port;
  uint16_t dest_port;
  uint32_t seq_num;
} tcp_header_t;

typedef union PacketHeader {
  tcp_header_t tcp_header;
  uint8_t raw[8];
} packet_header_t;