#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    con.query("CREATE TABLE IF NOT EXISTS \
        archive_2013(haiku_text VARCHAR(120), date_written CHAR(22))")

    fh = File.open(ARGV[0])
    @date_row = true
    @haiku_text = ""
    @date_written = "<i>"

# remove blank lines from file

    while( !fh.eof)
        line = fh.readline.chomp
# remove leading and trailing blanks
        line.strip!
# skip empty lines
        next if line == ''
# convert tab chars to blanks
        line.gsub!(/\t/,' ')
# convert apostrophe char to HTML code
        line.gsub!(/'/,'&#8217;')
# substitute a single blank for a sequence of blanks
        line.squeeze!(' ')
# insert line into table
        if @date_row == true
           @date_written << line
           @date_written << '</i><br>'
           @date_row = false
        else
           @haiku_text << line 
           @haiku_text << '<br>' 
        end
    end
#   puts @haiku_text
#   puts @date_written
    con.query("INSERT archive_2013(haiku_text, date_written) \
        VALUES('#{@haiku_text}', '#{@date_written}')")
    fh.close
    exit(0)

rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
