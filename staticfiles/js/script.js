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
    }

    if (categoryField) {
        categoryField.addEventListener('change', setTaskTypeFromCategory);
        setTaskTypeFromCategory();
    }
});
