"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        ## APPROACH : BUFFER READING ##
        ## 1. dont get confused with question description, our final buf will have min( n, all the characters that are in file)
        ## 2. At any point buf4, will maximum of 4 characters or count returned from the read4.
        ## 3. As I can read utmost 4 chars at a time, I create an array of size 4 and pass it to the function read4(buf4). That read4 function will fill my buf4 and returns the count how many characters it filled.
        ## 4. I take those buf4 chars filled and append it to my final buf.
        
        buf4 = [''] * 4         
        read = 0
        while read < n: 
            count = read4(buf4)             # Read file into buf4 && count -> num of chars in buf4
            if not count: break             # no of chars to read, EOF
            count = min(count, n - read)    # if n = 5 and file size is 8, in second read you have to take only n-read i.e 5-4 = 1
            buf[read:] = buf4[:count]       # Copy from buf4 to buf.
            read += count
        return read                         # we have return total num of characters read
        
        
        
        # Each byte is considered to have 8 bits in this context. 
        # Since there are 4 bytes, that means 4 × 8 bits = 32 bits are available for storing a number.
        # Because of the physical implementation, loading 4 bytes in DDR is faster than to load 1 byte 4 times.
        # On the majority of computers today, collection of 4 bytes, or 32 bits, is called a word. 
        # Most modern CPUs are optimized for the operations with words.