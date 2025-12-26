# test_todo_manager.py
import unittest
from todo_manager import TodoManager


class TestTodoManager(unittest.TestCase):
    """测试 TodoManager 类的功能。"""

    def setUp(self):
        """在每个测试方法运行前执行，用于设置测试环境。"""
        self.manager = TodoManager()
        # 先添加两个任务供后续测试使用
        self.manager.add_todo("学习Python")
        self.manager.add_todo("编写Jenkins流水线")

    def test_add_todo_valid(self):
        """测试正常添加任务。"""
        result = self.manager.add_todo("阅读一本书")
        self.assertEqual(result, "已添加任务: 阅读一本书 (ID: 3)")
        self.assertEqual(len(self.manager.list_todos()), 3)

    def test_add_todo_empty(self):
        """测试添加空任务时应抛出异常。"""
        with self.assertRaises(ValueError):
            self.manager.add_todo("")
        with self.assertRaises(ValueError):
            self.manager.add_todo("   ")

    def test_list_todos(self):
        """测试列出所有任务。"""
        todos = self.manager.list_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0]['task'], "学习Python")
        self.assertEqual(todos[1]['task'], "编写Jenkins流水线")

    def test_complete_todo_valid(self):
        """测试正常完成任务。"""
        result = self.manager.complete_todo(1)
        self.assertEqual(result, "恭喜！已完成任务: '学习Python'")
        # 检查任务状态是否已更新
        self.assertTrue(self.manager.list_todos()[0]['done'])

    def test_complete_todo_invalid_id(self):
        """测试完成一个不存在的ID时应抛出异常。"""
        with self.assertRaises(ValueError):
            self.manager.complete_todo(99)
        with self.assertRaises(ValueError):
            self.manager.complete_todo(0)

    def test_clear_all(self):
        """测试清空所有任务。"""
        result = self.manager.clear_all()
        self.assertEqual(result, "所有待办事项已清空。")
        self.assertEqual(len(self.manager.list_todos()), 0)


if __name__ == '__main__':
    # 运行单元测试
    unittest.main(verbosity=2)