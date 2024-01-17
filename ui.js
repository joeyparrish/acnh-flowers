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
  // tabs.  It is generated as part of the tabs element for convenience in the
  // templating system.
  document.getElementById('panels').appendChild(input.tabPanel);
}

// When the hash changes, pick the matching tab, or fall back to the first one.
function pickTab() {
  for (const input of inputs) {
    input.tabPanel.classList.remove('shown');
  }

  const targetId = 'tab-' + location.hash.substr(1);  // drop #
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
