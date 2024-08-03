There was a base64 encoded string in the metadata through which we got the flag.

```
┌──(kali㉿kali)-[~/Desktop/pico]
└─$ exiftool ukn_reality.jpg   
ExifTool Version Number         : 12.76
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:02:16 04:10:21+05:30
File Access Date/Time           : 2024:08:03 21:34:32+05:30
File Inode Change Date/Time     : 2024:08:03 21:34:28+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
                                                                                                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/pico]
└─$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_a6df8db8}
```

Flag:
```
picoCTF{ME74D47A_HIDD3N_a6df8db8}
```