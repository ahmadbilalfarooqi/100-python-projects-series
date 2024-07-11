'''
03-Project-Bitmap-Message
This program uses a multiline string as a
bitmap, a 2D image with only two possible
colors for each pixel, to determine how it
should display a message from the user. In this
bitmap, space characters represent an empty space,
and all other characters are replaced by characters in
the users message. The provided bitmap resembles
a world map, but you can change this to any image
you like. The binary simplicity of the space-ormessage-characters system makes it good for beginners.
Try experimenting with different messages to
see what the results look like!
'''

import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# you can copy and paste below line of bitmap ⬇️⬇️


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................

"""
print("Bitmap Message, by Ahmad Bilal <ahmadbilal20152016@gmail.com>")
print("Enter the message to display with the bitmap.")

message = input('> ')
if message == '':
    sys.exit()


# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # print a character from the message:
            print(message[i % len(message)], end='')
    print()  # print a newline.
