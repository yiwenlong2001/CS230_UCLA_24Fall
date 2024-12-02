#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <grammar_name> <code_file>"
    exit 1
fi

GRAMMAR_NAME=$1
CODE_FILE=$2

# 文件路径配置
G4_FILE="./g4_folder/${GRAMMAR_NAME}.g4"
INPUT_CODE="./code_folder/${CODE_FILE}"
OUTPUT_DIR="./inter_folder/${GRAMMAR_NAME}"

# 检查语法文件和输入代码文件是否存在
if [ ! -f "$G4_FILE" ]; then
    echo "Error: Grammar file $G4_FILE not found!" | tee -a log.txt
    exit 1
fi

if [ ! -f "$INPUT_CODE" ]; then
    echo "Error: Code file $INPUT_CODE not found!" | tee -a log.txt
    exit 1
fi

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 使用 ANTLR 生成解析器
java -jar antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 "$G4_FILE" -o "$OUTPUT_DIR" 2>&1 | tee -a log.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to generate parser from $G4_FILE" | tee -a log.txt
    exit 1
fi

LEXER_FILE="${OUTPUT_DIR}/${GRAMMAR_NAME}Lexer.py"
PARSER_FILE="${OUTPUT_DIR}/${GRAMMAR_NAME}Parser.py"

if [ ! -f "$LEXER_FILE" ] || [ ! -f "$PARSER_FILE" ]; then
    echo "Error: Parser files not generated successfully!" | tee -a log.txt
    exit 1
fi

PYTHONPATH="$OUTPUT_DIR" python match_code.py "$GRAMMAR_NAME" "$INPUT_CODE" 2>&1 | tee -a log.txt

if [ $? -ne 0 ]; then
    echo "Error: Matching process failed!" | tee -a log.txt
    exit 1
fi

echo "Process completed successfully. Results saved to log.txt" | tee -a log.txt
