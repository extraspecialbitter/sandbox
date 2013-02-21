#!/usr/bin/env ruby

puts "What's your favorite number?"
number = gets.chomp
output_number = number.to_i + 1
puts output_number.to_s + ' is a bigger and better favorite number.'
