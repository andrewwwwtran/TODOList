document.addEventListener('DOMContentLoaded', () =>{
  const container = document.querySelector('.container')

  // function to fetch and display tasks
  async function fetchTasks(){
    try{
      const response = await fetch('http://localhost:5000/api/todolist');
      const tasks = await response.json();

      // clear the container
      container.innerHTML = '';

      // display tasks in the container
      tasks.forEach((task) => {
        const taskElement = document.createElement('div');
        taskElement.innerHTML = `
          <input type="checkbox" ${task.completed ? 'checked' : ''}>
          <span>${task.text}</span>
        `;
        container.appendChild(taskElement);
      });
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  }
  fetchTasks();
});

// function to delete tasks
function deleteTask(taskId){
  fetch('/delete-task',{
    method: 'POST',
    body: JSON.stringify({taskId: taskId})
  }).then((_res) => {
    window.location.href = '/';
  });
}