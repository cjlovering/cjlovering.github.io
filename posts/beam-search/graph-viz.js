// Animates the @images a dictionary of file_name to image, which corresponds
// to the list of images @file_names.   
const animate = (images, file_names) => {  
   const WIDTH = 350;

   const buttons = d3.select('#target')
    .append("svg")
    .attr("width", WIDTH)
    .attr("height", 40);
  const canvas = d3.select('#target2')
    .append("svg")
    .attr("width", WIDTH)
    .attr("height", 425);

  // Shows the given image @i, appending it to the canvas.
  const show = i => {
    const img = images[file_names[i]];
    canvas.selectAll('svg').remove();
    canvas.node().appendChild(img);
  }

  // Add buttons which on click will show the corresponding step of the search.
  buttons.selectAll("circle")
    .data([0,1,2,3])
    .enter()
    .append('circle')
    .attr('r', 15)
    .attr('stroke', 'grey')
    .attr('fill', 'white')
    .attr('cx', d => { return d*70 + 65; } )
    .attr('cy', 17)
    .on("mouseover", d => show(d));

  // By default, show the full search graph.
  show(4);
}

// Loads image from the file path, and then saves the image with the 
// given saveImage callback.
const getImage = function(file_path, saveImage) {
  d3.xml(file_path).mimeType("image/svg+xml").get((error, xml) => {
    if (error) throw error;
    const svg = xml.documentElement;
    svg.setAttribute("height", "400px");
    svg.setAttribute("preserveAspectRatio", "xMinYMin meet");
    svg.id = file_path;
    saveImage(file_path, svg);
  });
}


// Load all the images, given @file_names. Store them into a dictionary, 
// file_name to svg object, for future manipulation.
const getImages = function(file_names) {
  let images = {};
  const saveImage = (file_path, img) => {
    images[file_path] = img;
    if (Object.keys(images).length >= file_names.length) {
      animate(images, file_names);
    }
  }
  file_names.forEach(name => getImage(name, saveImage));
  return images;
}

const file_names = [
  '/_static/images/002/beam-search-graph-01.svg',
  '/_static/images/002/beam-search-graph-02.svg',
  '/_static/images/002/beam-search-graph-03.svg',
  '/_static/images/002/beam-search-graph-04.svg',
  '/_static/images/002/beam-search-graph-05.svg'
];
getImages(file_names);