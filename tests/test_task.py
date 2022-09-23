import pytest
from unittest.mock import patch
from pytest_mock.plugin import MockerFixture

from myproject.task import add
import myproject

def test_celery_task_success_local(celery_app, celery_worker, mocker:MockerFixture):
    on_success_mocked = mocker.patch("myproject.task.MyTask.on_success")
    before_start_mocked = mocker.patch("myproject.task.MyTask.before_start")
    
    test_task_id = "test_task_id"
    test_args = (1,2)

    add.apply(args=test_args, task_id=test_task_id).get()
    
    before_start_mocked.assert_called_once()
    before_start_mocked.assert_called_with(test_task_id, test_args, {})

    on_success_mocked.assert_called_once()
    on_success_mocked.assert_called_with(3, test_task_id, test_args, {})


def test_celery_task_success_in_memory(celery_session_app, celery_session_worker, mocker:MockerFixture):
    test_task_id = "test_task_id"
    test_args = (1,2)

    result = add.delay(*test_args).get()
    assert result == 3
