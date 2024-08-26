#!/bin/bash

# Command to run your Llama model
your_llama_command="$HOME/llama.cpp"

# Log file path
log_file="main.log"

# Define the Documents folder path
documents_folder="$HOME/Documents/automacao"

# Output file path in Documents
output_file="$documents_folder/last_five_lines.log"

# Run the Llama model and wait for it to finish
# Run the Llama model and wait for it to finish
$HOME/llama-cli -m your_model.gguf -p "You are a helpful assistant" -cnv

# After the command finishes, extract the last 5 lines from the log file
tail -n 5 "$log_file" > "$output_file"

echo "Last 5 lines copied to $output_file"
