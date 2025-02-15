document.addEventListener("DOMContentLoaded", function () {
  const groups = [
    { name: "Group 1", tabs: ["Tab 1", "Tab 2"] },
    { name: "Group 2", tabs: ["Tab 3", "Tab 4"] },
  ];

  const groupContainer = document.getElementById("groups");
  const groupCount = document.getElementById("group-count");
  const soundIndicator = document.getElementById("sound-indicator");

  function updateGroupCount() {
    groupCount.textContent = `Total Groups: ${groups.length}`;
  }

  function toggleGroupContent(event) {
    const content = event.currentTarget.nextElementSibling;
    content.style.display =
      content.style.display === "block" ? "none" : "block";
  }

  function renderGroups() {
    groups.forEach((group) => {
      const groupElement = document.createElement("div");
      groupElement.className = "group";

      const header = document.createElement("div");
      header.className = "group-header";
      header.textContent = group.name;
      header.addEventListener("click", toggleGroupContent);

      const content = document.createElement("div");
      content.className = "group-content";
      content.innerHTML = group.tabs.map((tab) => `<div>${tab}</div>`).join("");

      groupElement.appendChild(header);
      groupElement.appendChild(content);
      groupContainer.appendChild(groupElement);
    });
  }

  function playSound() {
    axios
      .post("/play-sound/", { file_path: "/path/to/your/soundfile.mp3" })
      .then((response) => {
        console.log(response.data.message);
        soundIndicator.style.display = "block";
        setTimeout(() => {
          soundIndicator.style.display = "none";
        }, 3000); // Flash for 3 seconds
      })
      .catch((error) => {
        console.error("Error playing sound:", error);
      });
  }

  updateGroupCount();
  renderGroups();
});
