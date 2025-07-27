document.addEventListener('DOMContentLoaded', function() {
    var categoryField = document.getElementById('id_category');
    var taskTypeField = document.getElementById('id_task_type');
    var automationCategories = ['Appliances', 'Home Automation'];
    var userCategories = ['Entertainment', 'General Task'];

    function setTaskTypeFromCategory() {
        if (!categoryField || !taskTypeField) return;
        var selectedCategory = categoryField.options[categoryField.selectedIndex].text.trim();
        if (automationCategories.includes(selectedCategory)) {
            taskTypeField.value = 'automation';
        } else if (userCategories.includes(selectedCategory)) {
            taskTypeField.value = 'user';
        } else {
            // Default to user if unknown
            taskTypeField.value = 'user';
        }
        taskTypeField.setAttribute('readonly', 'readonly');
        // Also toggle recurrence fields if function exists
        if (typeof window.toggleRecurrenceFields === 'function') {
            window.toggleRecurrenceFields();
        }
    }

    function setCategoryFromTaskType() {
        if (!categoryField || !taskTypeField) return;
        var selectedTaskType = taskTypeField.value;
        if (selectedTaskType === 'automation') {
            // Set to first automation category
            for (var i = 0; i < categoryField.options.length; i++) {
                if (automationCategories.includes(categoryField.options[i].text.trim())) {
                    categoryField.selectedIndex = i;
                    break;
                }
            }
        } else if (selectedTaskType === 'user') {
            // Set to first user category
            for (var j = 0; j < categoryField.options.length; j++) {
                if (userCategories.includes(categoryField.options[j].text.trim())) {
                    categoryField.selectedIndex = j;
                    break;
                }
            }
        }
        // Also toggle recurrence fields if function exists
        if (typeof window.toggleRecurrenceFields === 'function') {
            window.toggleRecurrenceFields();
        }
    }

    if (categoryField) {
        categoryField.addEventListener('change', setTaskTypeFromCategory);
        setTaskTypeFromCategory();
    }
    if (taskTypeField) {
        taskTypeField.addEventListener('change', setCategoryFromTaskType);
    }
});
