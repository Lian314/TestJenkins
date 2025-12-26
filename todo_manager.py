# todo_manager.py
"""一个简单的待办事项管理器模块。"""


class TodoManager:
    """管理待办事项列表。"""

    def __init__(self):
        """初始化一个空的待办事项列表。"""
        self.todos = []

    def add_todo(self, task):
        """添加一个新的待办事项。

        Args:
            task (str): 要添加的任务描述。

        Returns:
            str: 成功添加的确认信息。
        """
        if not task or not task.strip():
            raise ValueError("任务内容不能为空。")
        todo_item = {"id": len(self.todos) + 1, "task": task.strip(), "done": False}
        self.todos.append(todo_item)
        return f"已添加任务: {task} (ID: {todo_item['id']})"

    def list_todos(self):
        """列出所有的待办事项。

        Returns:
            list: 包含所有待办事项字典的列表。
        """
        return self.todos

    def complete_todo(self, todo_id):
        """根据ID将一个待办事项标记为完成。

        Args:
            todo_id (int): 要完成的任务ID。

        Returns:
            str: 操作结果信息。

        Raises:
            ValueError: 当提供的ID无效或找不到对应任务时。
        """
        if not isinstance(todo_id, int) or todo_id < 1:
            raise ValueError("任务ID必须是一个正整数。")

        for item in self.todos:
            if item["id"] == todo_id:
                if item["done"]:
                    return f"任务(ID: {todo_id})已经是完成状态。"
                item["done"] = True
                return f"恭喜！已完成任务: '{item['task']}'"

        raise ValueError(f"未找到ID为 {todo_id} 的任务。")

    def clear_all(self):
        """清空所有待办事项。"""
        self.todos.clear()
        return "所有待办事项已清空。"