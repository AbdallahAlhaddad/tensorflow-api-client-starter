const imgWidth=224 //width of the image sent to server.
const imgHeight=224 //height of the image sent to server.
let predictionResults = [] //set by server response

const resultsList = document.getElementById("results")

function initializeFilePond(){

  //========== Register plugins ==========//
  FilePond.registerPlugin(
    FilePondPluginImagePreview,
    FilePondPluginImageResize,
    FilePondPluginFileValidateType
  )
  
   //========== Set Options ==========//
  FilePond.setOptions({
    acceptedFileTypes: ['image/png','image/jpeg','image/jpg'],
    imagePreviewHeight:390,
    imageResizeTargetWidth: imgWidth, 
    imageResizeTargetHeight: imgHeight,
    labelIdle: `Drag & Drop your picture or <span class="filepond--label-action">Browse</span>`,
    
    // see: https://pqina.nl/filepond/docs/patterns/api/server/#configuration
    server: {
      url: 'http://localhost:3000/api',
      process: {
          url: '/predict',
          method: 'POST',
          withCredentials: false,

          // server response:
          onload:(results)=>{
            predictionResults = JSON.parse(results)
          },

      },
      fetch:null,
      revert:null
    }
  })
  
  //=> Initialize:
  const inputElement = document.querySelector('input[type="file"]');
  const pond = FilePond.create(inputElement);
  
  //=> file finished processing event (show results in GUI):
  pond.on('processfile',()=>{
    resultsList.innerHTML='' //reset list

    for (const result of predictionResults) {
      const text= `Detected class "${result.class}" with confidence ${result.confidence}.`

      // Create the list item:
      const item = document.createElement('li');

      // Set its contents:
      item.appendChild(document.createTextNode(text));

      // Add it to the list:
      resultsList.appendChild(item);
    }
  })
}

initializeFilePond()






