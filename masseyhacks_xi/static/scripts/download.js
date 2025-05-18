document.getElementById("download_button").addEventListener("click", function () {
    const poster = document.getElementById("preview");

    html2canvas(poster, { useCORS: true, scale: 2 }).then(canvas => {
      const imgData = canvas.toDataURL("image/png");

      const { jsPDF } = window.jspdf;
      const pdf = new jsPDF({
        orientation: 'portrait',
        unit: 'px',
        format: [canvas.width, canvas.height]  // match canvas size
      });

      pdf.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
      pdf.save("album-poster.pdf");
    });
});