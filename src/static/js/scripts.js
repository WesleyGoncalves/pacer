// import "node_modules/popper.js/dist/umd/popper.min.js";
// const bootstrap = require('bootstrap') // synchronous, but cache the result
// import bootstrap from 'bootstrap'   // asynchronous, but do not cache

// Initialize all popovers
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [ ...popoverTriggerList ].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))


$(document).ready(function () {

  /**
   * Delete confirmation
   */
  $("[data-confirm-delete='popover']").on('click', function (event) {
    // event.preventDefault();
    const trigger = $(this);

    $(this).popover({
      placement: 'auto',
      // trigger: 'click',
      customClass: "popover-primary",
      html: true,
      sanitize: false,
      // container: event,
      // selector: '[rel="popover"]',
      title: "Excluir permanente",
      content: function () {
        const url = trigger.attr("data-href");

        return `
            <div class="row gy-3">
              <div class="col-12">
                Tem certeza que deseja <strong>excluir permanentemente</strong> esse registro e <strong>todos os seus dados</strong>?
              </div>
              <div class="col text-center">
                <button class="btn btn-primary w-100" onclick="$(this).closest('div.popover').hide('fade');">Cancelar</button>
              </div >
          <div class="col text-center">
            <a href="${ url }" class="btn btn-outline-primary w-100">
              <i class="bi bi-trash-fill pe-1"></i>
              Excluir
            </a>
          </div>
            </div >
          `
      },
    });

    $(this).popover('toggle')
  });



  /*
   * Evaluate form
   */

  /**
   * Project dropdown as a form select element
   */
  $("#project-dropdown a.dropdown-item").click(function (event) {
    // get project id and name
    const projectId = $(this).attr("data-project-id");
    const projectName = $(this).attr("data-project-name");
    const projectNSprints = $(this).attr("data-project-n-sprints");

    // write project id and name
    $("#project_id").val(projectId)
    $("#project_name").text(projectName);

    /**
     * Change the Sprints dropdown
     */
    let items = "";
    for (let i = 0; i < projectNSprints; i++) {
      const item = `<li> <a class="dropdown-item py-2" href="#" data-sprint-number="${ i + 1 }"> Sprint ${ i + 1 } </a> </li> `;
      items += item;
    }
    $("#sprints-dropdown-menu").html(items);

    $("#sprints-dropdown a.dropdown-item").click(function (event) {
      // get sprint number
      const sprintNumber = $(this).attr("data-sprint-number");

      // write sprint number
      $("#n_sprint").val(sprintNumber);
      $("#n_sprint_title").text(`Sprint ${ sprintNumber } `);
    });
  });

});
