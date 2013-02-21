#!/usr/bin/env ruby

fh = File.open(ARGV[0])

# remove blank lines from file

while( !fh.eof)
    line = fh.readline.chomp
    # remove leading and trailing blanks
    line.strip!
    # skip empty lines
    next if line == ''
    # convert tab chars to blanks
    line.gsub!(/\t/,' ')
    # substitute a single blank for a sequence of blanks
    line.squeeze!(' ')
    # add code to process line if needed
    puts line
end
fh.close
exit(0)

