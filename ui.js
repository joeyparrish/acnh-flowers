// Joey's ACNH Flower Guide
// Copyright (C) 2024 Joey Parrish
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

document.addEventListener('DOMContentLoaded', () => {
  // When a tab is selected, put the tab name in the URL hash.
  const inputs = Array.from(
      document.getElementById('tabs').querySelectorAll('input'));
  for (const input of inputs) {
    const tabId = input.id.replace('tab-', '');
    input.addEventListener('change', () => {
      location.hash = tabId;
    });
    // Find the associated panel.
    input.tabPanel = document.getElementById('panel-' + tabId);
    // Move it to the panel element so it flows correctly as separate from the
    // tabs.  It is generated as part of the tabs element for convenience in
    // the templating system.
    document.getElementById('panels').appendChild(input.tabPanel);
  }
  // Only now that we have moved everything, show the tabs and hide the loading
  // message.
  document.getElementById('tabs').classList.add('ready');
  document.getElementById('loading').classList.add('ready');

  // When we load the breeding layouts panel, if we are supposed to link to a
  // specific layout, we use IntersectionObserver to know when that layout is
  // visible and can be scrolled to. When that event fires, if scrollToLayout
  // is non-null, we scroll to the layout.
  let scrollToLayout = null;
  const breedingPanel = document.getElementById('panel-breeding-layouts');
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].intersectionRatio) {
      if (scrollToLayout) {
        const layoutElement = document.getElementById(scrollToLayout);
        layoutElement.scrollIntoView();
        scrollToLayout = null;
      }
    }
  }, {root: document.body});
  observer.observe(breedingPanel);

  // When the hash changes, pick the matching tab, or fall back to the first
  // one.
  function pickTab() {
    for (const input of inputs) {
      input.tabPanel.classList.remove('shown');
    }

    const hashValue = location.hash.substr(1);  // drop #
    let targetId;
    scrollToLayout = null;
    if (hashValue.startsWith('layout-')) {
      targetId = 'tab-breeding-layouts';
      scrollToLayout = hashValue;
    } else {
      targetId = 'tab-' + hashValue;
      window.scrollTo(0, 0);
    }

    const chosenInput =
        inputs.find(input => input.id == targetId) || inputs[0];
    chosenInput.checked = true;
    chosenInput.tabPanel.classList.add('shown');
  }

  const quickRef = document.getElementById('quick-ref');
  function setQuickRef() {
    document.body.classList.toggle('quick-ref', quickRef.checked);
    localStorage.setItem('acnh-flower-quick-ref', quickRef.checked);
  }
  quickRef.addEventListener('change', setQuickRef);
  // localStorage stores a string, so compare to that.
  quickRef.checked =
      (localStorage.getItem('acnh-flower-quick-ref', false) == 'true')
  setQuickRef();

  window.addEventListener('hashchange', pickTab);
  pickTab();
});
