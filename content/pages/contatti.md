Title: Contatti

Per contattarci compila il form di seguito, ti risponderemo il prima possibile!

<style>
.button {background-color: #95bc50;
  color:white;
  font-family: "Roboto";
  } /* green */ 
input {
  padding: 10px;
    line-height: 1.5;
    border-radius: 5px;
    border: 1px solid #ccc;
}
textarea {
    padding: 10px;
    line-height: 1.5;
    border-radius: 5px;
    border: 1px solid #ccc;
}
/* Set the size of the div element that contains the map */

#map {
  width: 80%;
  height: 400px;
}
</style>

<form method="post" action="https://www.flexyform.com/f/9e3ff9219ad05da10eba2174396d3637f04fdd58">
  <div class="form-row align-items-center">
    <div class="form-group">
      <input type="email" name="email" class="form-control" placeholder="Email" required="required">
    </div>
    <div class="form-group">
      <input type="text" name="name" class="form-control"  placeholder="Nome" required="required">
    </div>
    <div class="form-group">
      <input type="number" name="telefono" class="form-control" placeholder="Telefono">
    </div>
    <div class="form-group">
      <textarea name="messaggio" class="form-control" rows="4" cols="20" placeholder="Messaggio"></textarea>
    </div>
    <!--<button type="submit" class="btn btn-primary">Invia</button>-->
    <button type="submit" class="button">Invia</button>
  </div>
</form>

<!--<form method="post" action="https://www.flexyform.com/f/9e3ff9219ad05da10eba2174396d3637f04fdd58">
  <div class="form-row align-items-center">
    <div class="col-auto">
      <label class="sr-only" for="inlineFormInput">Nome</label>
      <input type="text" class="form-control mb-2" id="inlineFormInput" placeholder="Nome" required>
    </div>
    <div class="col-auto">
      <label class="sr-only" for="inlineFormInput">Email</label>
      <input type="text" class="form-control mb-2" id="inlineFormInput" placeholder="Email" required>
    </div>
    <div class="col-auto">
      <label class="sr-only" for="inlineFormInput">Telefono</label>
      <input type="number" class="form-control mb-2" id="inlineFormInput" placeholder="Telefono">
    </div>
    <div class="col-auto">
      <label class="sr-only" for="inlineFormInput">Messaggio</label>
      <input type="text" class="form-control mb-2" id="inlineFormInput" placeholder="Lascia qua il tuo messaggio">
    </div>
      <button type="submit" class="btn btn-primary mb-2">Invio</button>
    </div>
  </div>
</form>-->

<input type="text" style="visibility: hidden" value="" name="_empty_field"/>
<input type="hidden" name="_recaptcha" id="_recaptcha"/>
<script src="https://www.google.com/recaptcha/api.js?render=6Lf7UsoUAAAAACT2Z6gLyh7RTDfyYGxfZ-M4D0ph"></script>
<script src="https://www.flexyform.com/js/recaptcha.js"></script>

Se vuoi venire a trovarci, ci trovi al **[seguente indirizzo](https://www.google.com/maps/place/cooperativa+sociale+%22La+Prateria+%22/@46.0962766,8.3019482,15z/data=!4m5!3m4!1s0x0:0xab3f228bf463f90d!8m2!3d46.0962766!4d8.3019482)**.


 
<div id="map">
    <script>
      // Initialize and add the map
      function initMap() {
      // The location of Uluru
      var chiesa = {lat: 46.0962766, lng: 8.3019482};
      // The map, centered at Uluru
      var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 14.8, center: chiesa});
      // The marker, positioned at Uluru
      var marker = new google.maps.Marker({position: chiesa, map: map});
    }
    </script>
  <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCjuOWgCIRCY9i7W0ponf03SnyI5e6nGCs&callback=initMap">
  </script>
</div>

