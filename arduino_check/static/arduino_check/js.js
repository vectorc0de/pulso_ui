$(document).ready(function() {

  
  function LoadLines(canvasName1, timeVals)
  {      

      new Chart(document.getElementById(canvasName1, ), {
          type: 'bar',
          data: {
            labels: timeVals,
            datasets: [{
                type: "line",
                borderColor: "#8e5ea2",
                data: [408,547,675,734],
                fill: false
              }, {
                type: "line",
                borderColor: "#3e95cd",
                data: [133,221,783,2478],
                fill: false
              }, {
                type: "bar",
                backgroundColor: "rgba(0,0,0,0.2)",
                data: [408,547,675,734],
              }, {
                type: "bar",
                backgroundColor: "rgba(0,0,0,0.2)",
                backgroundColorHover: "#3e95cd",
                data: [133,221,783,2478]
              }
            ]
          },
          options: {
            title: {
              display: true,
              text: 'SPO2 & HeartRate Values'
            },
            legend: { display: false }
          }
      });

  }

  function loadSpo2(canvasName, spo2Vals, timeVals)
  {
      new Chart(document.getElementById(canvasName), {
          type: 'line',
          data: {
            labels: timeVals,
            datasets: [
              {
                label: "SPO2 Values",
                backgroundColor: "#79aec8",
                data: spo2Vals
              }
            ]
          }
      });    
  }

  function LoadPie2(divName, etiquetas, valuesLst)
  {


      new Chart(document.getElementById(divName), {
          type: 'doughnut',
          data: {
            labels: etiquetas,
            datasets: [
              {
                label: "Heart rates days",
                backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                data: valuesLst
              }
            ]
          },
          options: {

              type: "pie",
              options: {
                responsive: true,
                layout: {
                  padding: {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: 25
                  }
                }
              }


          }
      });
  }

  function loadLastLog(divName, dataPrm, timePrm)
  {

      const ctx = document.getElementById(divName).getContext('2d');
      const myChart = new Chart(ctx, {
          type: 'bar',
          data: {
              labels: timePrm,
              datasets: [{
                  label: 'Heart Rate average',
                  data: dataPrm,
                  backgroundColor: "#79aec8",
                  borderColor:  "#79aec8",
                  borderWidth: 1
              }]
          },
          options: {

              responsive: true,

          }
      });
  }

  function GetPatient(id)
  {      

      $.ajax({
      url: "patients/report/" + id + "/0/null/0",
      type: "GET",
      dataType: "json",
      success: (jsonResponse) => {

        var hrList = [];
        var hrListCut = [];
        var timeValsCut = [];
        var spo2List = [];
        var timeVals = [];        
        var index = 0x0;

        jsonResponse.dats.forEach(dats => {

          hrList.push(dats.hr);

          if(index>5 && index<12)
          {
            hrListCut.push(dats.hr);
            timeValsCut.push(dats.finalDelta);
          }

          timeVals.push(dats.finalDelta);
          spo2List.push(dats.spo2);

          index++;


        });
  
        loadLastLog('lastLogs', hrList, timeVals);
        loadSpo2('canvasLineSpo2', spo2List, timeVals);

  
        console.log(hrListCut);
        LoadPie2('pie1', timeValsCut, hrListCut);

      },
      error: () => console.log("Failed to fetch chart filter options!")
    });    

  }


  function GetPatients()
  {

      $.ajax({
      url: "patients/filter-options/",
      type: "GET",
      dataType: "json",
      success: (jsonResponse) => {

        jsonResponse.patients.forEach(patient => {

          $("#cmbPatient").append(new Option(patient[0], patient[1]));

        });
  

      },
      error: () => console.log("Failed to fetch chart filter options!")
    });    
  }


  $("#patientForm").on("submit", (event) => {
    event.preventDefault();

    var idUser = $("#patientForm option:selected").val()
    console.log("ID:: " + idUser)
    GetPatient(idUser);

  });  

  GetPatient(6);
  GetPatients();

  }); // first document.ready