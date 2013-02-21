#!/usr/bin/env ruby

fname = ARGV[0]
start_column = 3
end_column = 5

target_range = (start_column-1)..(end_column-1)

IO.foreach(fname) do |line|
  if line.match(/<strong>Date:<\/strong>/)
    pieces = line.split(" ")

    puts pieces[target_range].join("-")
  end
end
