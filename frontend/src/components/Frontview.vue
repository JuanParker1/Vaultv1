<template>
  <div id="app">
    <div class="assessment-container container">
        <div class="row">
            <div class="col-md-6 form-box">
                        <div class="form-top">
                            <div class="form-top-left">
                                <h3 class="text-left">Deposit Confirmation</h3>
                                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit
                                </p> -->
                            </div>
                        </div>
                        <div class="form-bottom">
                          <div class="form-group">
                                <label for="">Api Key</label>
                                <input type="text"  v-model="user.api_key" name="amount" placeholder="Api Key" class="form-email form-control" id="amount" required>
                            </div>
                            <div class="form-group">
                                <label for="">Seceret Key</label>
                                <input type="text"  v-model="user.seceret_key" name="amount" placeholder="Seceret Key" class="form-email form-control" id="amount" required>
                            </div>
                            <div class="form-group">
                                <label for="">User Deposit Confirmation</label>
                                <select class="form-control"  v-model="user.coin">
                                    <option selected="selected">ETHRIUM</option>
                                    <option>BTC</option>
                                    <option>MATIC</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="">Amount</label>
                                <input type="number"  v-model="user.amount" name="amount" placeholder="Amount" class="form-email form-control" id="amount" required>
                            </div>
                             <div class="form-group">
                                <label for="">Address</label>
                                <input type="text" name="amount" readonly  value="0x7aa2a5f3592963fe9e35bf419565a8a483dffe75" class="form-email form-control" id="amount" required>
                            </div>
                            
                            <button type="button"  @click="submit()" class="btn btn-next mt-3">Save</button>
                        </div>                    
            </div>
        </div>
    </div>
  </div>
</template>
<script>
 import axios from "axios";
export default {
  data() {
    return {
      user: {
        api_key: "",
        seceret_key: "",
        amount:"",
        coin:""
      },
    };
  },
  methods: {
    submit: function () {
      const path = "http://127.0.0.1:5000/dataentry";
      axios
        .post(path, {
           api_key: this.user.api_key,
        seceret_key: this.user.seceret_key,
        amount:this.user.amount,
        coin:this.user.coin
        })
        .then((response) => {
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Lato&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Castoro&display=swap");
#app {
  font-family: "Lato", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#input-group-1 {
  margin-left: 25%;
  margin-bottom: 20px;
  width: 50%;
  padding-left: 80px;
  margin-top: 50px;
  font-weight: bold;
}
h3 {
  margin-top: 20px;
  font-family: "Castoro", serif;
}

</style>

    <style>
        input[type="text"],
input[type="email"],
input[type="date"],
select.form-control {
    height: 50px;
    margin: 0;
    padding: 0 20px;
    vertical-align: middle;
    background: #f8f8f8;
    border: 3px solid #ddd;
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 50px;
    color: #888;
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
    border-radius: 4px;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    -o-transition: all .3s;
    -moz-transition: all .3s;
    -webkit-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

input[type="file"] {
    height: 35px;
    margin: 0;
    padding: 0 20px;
    vertical-align: bottom;
    background: #f8f8f8;
    border: 3px solid #ddd;
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 30px;
    color: #888;
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
    border-radius: 4px;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    -o-transition: all .3s;
    -moz-transition: all .3s;
    -webkit-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

input[type=radio] {
    margin-top: 8px !important;
}

textarea,
textarea.form-control {
    padding-top: 10px;
    padding-bottom: 10px;
    line-height: 30px;
}

input[type="text"]:focus,
input[type="password"]:focus,
textarea:focus,
textarea.form-control:focus {
    outline: 0;
    background: #fff;
    border: 3px solid #ccc;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
}

input[type="text"]:-moz-placeholder,
input[type="password"]:-moz-placeholder,
textarea:-moz-placeholder,
textarea.form-control:-moz-placeholder {
    color: #888;
}

input[type="text"]:-ms-input-placeholder,
input[type="password"]:-ms-input-placeholder,
textarea:-ms-input-placeholder,
textarea.form-control:-ms-input-placeholder {
    color: #888;
}

input[type="text"]::-webkit-input-placeholder,
input[type="password"]::-webkit-input-placeholder,
textarea::-webkit-input-placeholder,
textarea.form-control::-webkit-input-placeholder {
    color: #888;
}

button.btn {
    height: 50px;
    margin: 0;
    padding: 0 20px;
    vertical-align: middle;
    background: #26A69A;
    ;
    border: 0;
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 50px;
    color: #fff;
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
    border-radius: 4px;
    text-shadow: none;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    -o-transition: all .3s;
    -moz-transition: all .3s;
    -webkit-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

button.btn:hover {
    opacity: 0.6;
    color: #fff;
}

button.btn:active {
    outline: 0;
    opacity: 0.6;
    color: #fff;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
}

button.btn:focus {
    outline: 0;
    opacity: 0.6;
    background: #26A69A;
    ;
    color: #fff;
}

button.btn:active:focus,
button.btn.active:focus {
    outline: 0;
    opacity: 0.6;
    background: #26A69A;
    ;
    color: #fff;
}


/*style.css**/

body {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    font-weight: 300;
    color: #888;
    line-height: 30px;
    text-align: center;
}

strong {
    font-weight: 500;
}

a,
a:hover,
a:focus {
    color: #26A69A;
    ;
    text-decoration: none;
    -o-transition: all .3s;
    -moz-transition: all .3s;
    -webkit-transition: all .3s;
    -ms-transition: all .3s;
    transition: all .3s;
}

h1,
h2 {
    margin-top: 10px;
    font-size: 38px;
    font-weight: 100;
    color: #555;
    line-height: 50px;
}

h3 {
    font-size: 22px;
    font-weight: 300;
    color: #555;
    line-height: 30px;
}

::-moz-selection {
    background: #26A69A;
    ;
    color: #fff;
    text-shadow: none;
}

::selection {
    background: #26A69A;
    ;
    color: #fff;
    text-shadow: none;
}

.btn-link-1 {
    display: inline-block;
    height: 50px;
    margin: 0 5px;
    padding: 16px 20px 0 20px;
    background: #26A69A;
    font-size: 16px;
    font-weight: 300;
    line-height: 16px;
    color: #fff;
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
    border-radius: 4px;
}

.btn-link-1:hover,
.btn-link-1:focus,
.btn-link-1:active {
    outline: 0;
    opacity: 0.6;
    color: #fff;
}

.btn-link-2 {
    display: inline-block;
    height: 50px;
    margin: 0 5px;
    padding: 15px 20px 0 20px;
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid #fff;
    font-size: 16px;
    font-weight: 300;
    line-height: 16px;
    color: #fff;
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
    border-radius: 4px;
}

.btn-link-2:hover,
.btn-link-2:focus,
.btn-link-2:active,
.btn-link-2:active:focus {
    outline: 0;
    opacity: 0.6;
    background: rgba(0, 0, 0, 0.3);
    color: #fff;
}


/***** Top content *****/

.form-box {
    padding-top: 40px;
    font-family: 'Roboto', sans-serif !important;
}

.form-top {
    overflow: hidden;
    padding: 0 25px 15px 25px;
    background: #26A69A;
    -moz-border-radius: 4px 4px 0 0;
    -webkit-border-radius: 4px 4px 0 0;
    border-radius: 4px 4px 0 0;
    text-align: left;
    color: #fff;
    transition: opacity .3s ease-in-out;
}

.form-top h3 {
    color: #fff;
}

.form-bottom {
    padding: 25px 25px 30px 25px;
    background: #eee;
    -moz-border-radius: 0 0 4px 4px;
    -webkit-border-radius: 0 0 4px 4px;
    border-radius: 0 0 4px 4px;
    text-align: left;
    transition: all .4s ease-in-out;
}

.form-bottom:hover {
    -webkit-box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
}

form .form-bottom button.btn {
    min-width: 105px;
}

form .form-bottom .input-error {
    border-color: #d03e3e;
    color: #d03e3e;
}

form.registration-form fieldset {
    display: none;
}
    </style>