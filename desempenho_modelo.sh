#!/bin/bash
# Command to run your Llama model
your_llama_command="$HOME/llama.cpp"

# Log file path
log_file="main.log"

# Define the Documents folder path
documents_folder="$HOME/Documents/automacao"

# Output file path in Documents
cd
cd Documents/automacao
chmod u+w ~/Documents/automacao/
output_file="$documents_folder/last_five_lines1.txt"

cd 
cd llama.cpp
# Run the Llama model and wait for it to finish
./llama-cli -m meta-llama-3.1-8b-instruct-q4_0.gguf -p "You are a helpful assistant" -cnv

# After the command finishes, extract the last 5 lines from the log file
tail -n 5 "$log_file" >> "$output_file"

echo "Last 5 lines copied to $output_file"
