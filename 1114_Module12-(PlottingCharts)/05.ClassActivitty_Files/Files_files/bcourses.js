(function(window, $) {
  'use strict';

  var loadCanvasCustomization = function() {
    window.CALCENTRAL = 'https://junction.berkeley.edu';

    // Ensure the bCourses development and test servers are pointing to the correct
    // CalCentral instance when a copy of production is made
    if (window.location.origin === 'https://ucberkeley.beta.instructure.com') {
      window.CALCENTRAL = 'https://junction-dev.berkeley.edu';
    } else if (window.location.origin === 'https://ucberkeley.test.instructure.com') {
      window.CALCENTRAL = 'https://junction-qa.berkeley.edu';
    }

    // Load the JavaScript customizations
    $.ajax({
      'dataType': 'script',
      'url': window.CALCENTRAL + '/static/canvas/canvas-customization.js',
      'cache': true
    });

    // Load the CSS customizations
    var css = $('<link>', {
      'rel': 'stylesheet',
      'type': 'text/css',
      'href': window.CALCENTRAL + '/static/canvas/canvas-customization.css'
    });
    $('head').append(css);
  };

  if (document.readyState === 'complete' || (document.readyState !== 'loading' && !document.documentElement.doScroll)) {
    loadCanvasCustomization();
  } else {
    document.addEventListener('DOMContentLoaded', loadCanvasCustomization);
  }

})(window, window.$);

////////////////////////////////////////////////////
// DESIGN TOOLS CONFIG                            //
////////////////////////////////////////////////////
// Copyright (C) 2017  Utah State University
var DT_variables = {
        iframeID: '',
        // Path to the hosted USU Design Tools
        path: 'https://designtools.ciditools.com/',
        templateCourse: '1492983',
        // OPTIONAL: Button will be hidden from view until launched using shortcut keys
        hideButton: true,
       // OPTIONAL: Limit by course format
       limitByFormat: false, // Change to true to limit by format
       // adjust the formats as needed. Format must be set for the course and in this array for tools to load
       formatArray: [
            'online',
            'on-campus',
            'blended'
        ],
        // OPTIONAL: Limit tools loading by users role
        limitByRole: false, // set to true to limit to roles in the roleArray
        // adjust roles as needed
        roleArray: [
            'student',
            'teacher',
            'admin'
        ],
        // OPTIONAL: Limit tools to an array of Canvas user IDs
        limitByUser: false, // Change to true to limit by user
        // add users to array (Canvas user ID not SIS user ID)
        userArray: [
            '1234',
            '987654'
        ]
};

// Run the necessary code when a page loads
$(document).ready(function () {
    'use strict';
    // This runs code that looks at each page and determines what controls to create
    $.getScript(DT_variables.path + 'js/master_controls.js', function () {
        console.log('master_controls.js loaded');
    });
});
////////////////////////////////////////////////////
// END DESIGN TOOLS CONFIG                        //
////////////////////////////////////////////////////

/* ALLY */

/**
 * Load custom Ally JavaScript
 */

window.ALLY_CFG = {
 'baseUrl': 'https://prod.ally.ac',
 'clientId': 2,
 'lti13Id': '10720000000000611'
};
$.getScript(ALLY_CFG.baseUrl + '/integration/canvas/ally.js');

/* end Ally customization */
