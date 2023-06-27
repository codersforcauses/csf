<template>
  <img src="@/assets/Footer-min.jpeg" class="border"/>
  <v-toolbar dark app color="black" class="hidden-sm-and-down mt-2">
    <img alt="CSF Logo"  src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
    <v-toolbar-title class="hidden-md-and-down">Community Spirit Foundation</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn v-for="item in menu" :key="item.icon" :to="item.link" flat>{{
        item.title
      }}</v-btn>
    </v-toolbar-items>
  </v-toolbar>
  <v-toolbar dark app color="black" class="hidden-md-and-up mt-2">
    <img alt="CSF Logo"  src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
    <v-spacer></v-spacer>
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-up-transition">
      <template v-slot:activator="{ props }" >
        <button v-bind="props" class="hidden-md-and-up">
          <i :class="'fa fa-bars  fa-lg'"></i>
        </button>
      </template>
      <v-card class="overall mt-2">
        <v-toolbar dark app color="black" class="mt-2">
          <img alt="CSF Logo"  src="@/assets/CSF_Logo_WHITE.png" width="125" height="60" />
          <v-spacer></v-spacer>
          <v-btn icon @click.native="dialog = false" class="hidden-md-and-up">
            <i :class="'fa fa-times fa-lg'"></i>
          </v-btn>
        </v-toolbar>
        <v-list class="listItem"> 
          <v-list-item
            v-for="(item, index) in menu"
            :key="index"
            :value="index"
          >
            <template v-slot:prepend>
              <v-icon v-if="item.icon">{{item.icon}}</v-icon>
            </template>
            <v-list-item-title >{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card>
    </v-dialog>
  </v-toolbar>
</template>

<script>
export default {
  data() {
    return {
      menu: [
        { icon: "fa fa-address-card  fa-lg", title: "About Us" },
        { icon: "fa fa-chart-line  fa-lg", title: "Dashboard" },
        { icon: "fa fa-trophy  fa-lg", title: "Challenges" },
        { icon: "fa fa-users  fa-lg", title: "Team Page" },
        { icon: "fa fa-calendar  fa-lg", title: "Events" },
        { icon: "fa fa-star  fa-lg", title: "Leaderboards" },
        { icon: "fa fa-sign-in-alt  fa-lg", title: "Login" },
        { icon: "fa fa-pen-square  fa-lg", title: "Sign Up" },
      ],
      dialog: false
    };
  },

  methods: {
    menuItems() {
      return this.menu;
    },
  }
};
</script>
<style>
@import url('https://use.fontawesome.com/releases/v5.9.0/css/all.css');
.hidden-md-and-up {
  padding-right: 3%;
}
.listItem{
  color: white;
  background-color: black;
}
.overall{
  background-color: black;
}
.border {
  height: 10px;
  width: 100%;
  overflow: hidden;
  position: absolute;
  top: 0;
  left: 0;
}
</style>