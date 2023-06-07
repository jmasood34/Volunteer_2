 // Checkbox validation script
const checkboxes = document.querySelectorAll('input[type="checkbox"]')
    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('click', () => {
          if (checkbox.checked) {
              checkboxes.forEach((c) => {
                  if (c !== checkbox) {
                    c.checked = false
          }
        })
      }
    })
  })