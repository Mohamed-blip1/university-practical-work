CC = gcc
CFLAGS = -Wall -Werror -Wextra -Iinclude
# CFLAGS = -Iinclude

TARGET = main

SRC_DIR = src
OBJ_DIR = build

SRCS = $(wildcard $(SRC_DIR)/*c )
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o )

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | build
	$(CC) $(CFLAGS) -c $< -o $@

build:
	mkdir -p build

run:$(TARGET)
	./$(TARGET)

clean:
	rm -r main build/*

.PHONY: clean run clean
