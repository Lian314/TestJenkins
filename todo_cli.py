# todo_cli.py
"""待办事项管理器的命令行界面。"""
from todo_manager import TodoManager


def main():
    manager = TodoManager()
    print("=== 简易待办事项管理器 ===")
    print("命令: add <任务>, list, done <ID>, clear, exit")

    while True:
        try:
            user_input = input("\n请输入命令: ").strip().split(' ', 1)
            command = user_input[0].lower()

            if command == "exit":
                print("再见！")
                break
            elif command == "add":
                if len(user_input) < 2:
                    print("错误：请使用 'add <任务描述>' 的格式。")
                else:
                    task = user_input[1]
                    result = manager.add_todo(task)
                    print(result)
            elif command == "list":
                todos = manager.list_todos()
                if not todos:
                    print("当前没有待办事项。")
                else:
                    print("\n当前待办事项:")
                    for item in todos:
                        status = "✓" if item["done"] else " "
                        print(f"  [{status}] {item['id']}: {item['task']}")
            elif command == "done":
                if len(user_input) < 2:
                    print("错误：请使用 'done <任务ID>' 的格式。")
                else:
                    todo_id = int(user_input[1])
                    result = manager.complete_todo(todo_id)
                    print(result)
            elif command == "clear":
                result = manager.clear_all()
                print(result)
            else:
                print("未知命令。请尝试: add, list, done, clear, exit")
        except ValueError as e:
            print(f"输入错误: {e}")
        except Exception as e:
            print(f"发生意外错误: {e}")


if __name__ == "__main__":
    main()