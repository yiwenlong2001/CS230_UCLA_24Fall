#!/bin/bash

# 检查输入文件是否存在
INPUT_CODE="./code_folder/expression.txt"
if [ ! -f "$INPUT_CODE" ]; then
    echo "Error: Input code file $INPUT_CODE not found!" | tee -a log_all.txt
    exit 1
fi

# 遍历 g4_folder 下所有的 .g4 文件
for G4_FILE in ./g4_folder/*.g4; do
    GRAMMAR_NAME=$(basename "$G4_FILE" .g4)
    OUTPUT_DIR="./inter_folder/${GRAMMAR_NAME}"

    echo "Processing grammar: $GRAMMAR_NAME" | tee -a log_all.txt

    # 创建输出目录
    mkdir -p "$OUTPUT_DIR"

    # 使用 ANTLR 生成解析器
    java -jar antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 "$G4_FILE" -o "$OUTPUT_DIR" 2>&1 | tee -a log_all.txt

    if [ $? -ne 0 ]; then
        echo "Error: Failed to generate parser from $G4_FILE" | tee -a log_all.txt
        continue
    fi

    # 检查解析器文件是否生成成功
    LEXER_FILE="${OUTPUT_DIR}/${GRAMMAR_NAME}Lexer.py"
    PARSER_FILE="${OUTPUT_DIR}/${GRAMMAR_NAME}Parser.py"

    if [ ! -f "$LEXER_FILE" ] || [ ! -f "$PARSER_FILE" ]; then
        echo "Error: Parser files not generated successfully for $GRAMMAR_NAME!" | tee -a log_all.txt
        continue
    fi

    # 调用 Python 脚本对 b.txt 的每一行进行匹配
    PYTHONPATH="$OUTPUT_DIR" python match_code_all.py "$GRAMMAR_NAME" "$INPUT_CODE" 2>&1 | tee -a log_all.txt
done

echo "Evaluation completed. Results saved to log_all.txt" | tee -a log_all.txt
