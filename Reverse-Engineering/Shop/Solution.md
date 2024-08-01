```
undefined8 main(void)

{
  undefined local_f8 [136];
  void *local_70;
  byte local_68 [16];
  undefined8 local_58;
  undefined8 local_50;
  undefined8 local_48;
  undefined8 local_40;
  byte local_2d;
  int local_2c;
  undefined4 local_28;
  int local_24;
  undefined local_1d;
  int local_1c;
  char *local_18;
  int local_10;
  int local_c;
  
  local_18 = "9rKFLE28b8IFNPIYt0WGD2fqosGh8oAft1zFPoW/ccL3a1IAgfZ/KVtrui2coyX+";
  local_48 = 0x756f7965766f6c69;
  <!-- local_40 = 0x3433323133323332; -->
  local_58 = 0xe5ffe9f5e6fffcf9;
  local_50 = 0xa4a3a2a1a3a2a3a2;
  local_1c = 0x10;
  local_1d = 0;
  printf("XORed result: ");
  local_10 = 0;
  for (local_c = 0; local_c < local_1c; local_c = local_c + 1) {
    local_2d = *(byte *)((long)&local_58 + (long)local_c) ^ 0x5a;
    local_68[local_10] = local_2d;
    local_10 = local_10 + 1;
  }
  puts((char *)local_68);
  local_24 = 0x5a;
  local_28 = base64_decode(local_18,&local_70);
  local_2c = aes_decrypt(local_70,local_28,&local_48,local_f8);
  local_f8[local_2c] = 0;
  puts("Decrypted text is:");
  if (local_24 == 0xd0) {
    pFlag(local_f8);
  }
  else {
    puts("Lollololololollloo");
  }
  free(local_70);
  return 0;
}

```