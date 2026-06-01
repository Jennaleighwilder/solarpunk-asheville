/*
 * Shared image/video enhancer for the Solarpunk mockups.
 * Injects real microscope imagery (and a hero video) into each design's
 * placeholder regions without touching the original bespoke layouts.
 */
(function () {
  var IMG = "assets/img/";
  var VID = "assets/video/biosphere_reel.mp4";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Per-design configuration, keyed by the leading file number.
  var CONFIG = {
    "01": { heroBg: "micro_mycelium_network.png", overlay: "rgba(6,18,11,0.60)" },
    "02": { panel: ".hero-right", img: "micro_pollen_sem.png" },
    "03": { panel: ".hero-right", img: "micro_diatoms_algae.png" },
    "04": { panel: ".hero-right", img: "micro_leaf_chloroplasts.png" },
    "05": { heroBg: "micro_mycelium_network.png", overlay: "rgba(0,0,0,0.55)", panel: ".visual-box", img: "micro_mycelium_network.png" },
    "06": { panel: ".hero-bg", img: "micro_diatoms_algae.png", panelOverlay: "rgba(244,239,228,0.30)" },
    "07": { video: ".hero-video-placeholder", poster: "micro_leaf_chloroplasts.png" },
    "08": { panel: ".hero-right", img: "micro_mycelium_network.png" }
  };

  function pageKey() {
    var m = (location.pathname || "").match(/(\d{2})_/);
    return m ? m[1] : null;
  }

  function styleCover(el, imageCss) {
    el.style.backgroundImage = imageCss;
    el.style.backgroundSize = "cover";
    el.style.backgroundPosition = "center";
    el.style.backgroundRepeat = "no-repeat";
  }

  function apply() {
    var key = pageKey();
    var cfg = key && CONFIG[key];
    if (!cfg) return;

    // Full-bleed hero background (dark designs) with a legibility overlay.
    if (cfg.heroBg) {
      var hero = document.querySelector(".hero");
      if (hero) {
        styleCover(hero, "linear-gradient(" + cfg.overlay + "," + cfg.overlay + "), url(" + IMG + cfg.heroBg + ")");
      }
    }

    // Dedicated visual panel (light designs / side panels).
    if (cfg.panel && cfg.img) {
      var panel = document.querySelector(cfg.panel);
      if (panel) {
        var img = "url(" + IMG + cfg.img + ")";
        if (cfg.panelOverlay) {
          img = "linear-gradient(" + cfg.panelOverlay + "," + cfg.panelOverlay + ")," + img;
        }
        styleCover(panel, img);
      }
    }

    // Hero video region (the editorial design literally has a video placeholder).
    if (cfg.video) {
      var slot = document.querySelector(cfg.video);
      if (slot) {
        if (reduce) {
          styleCover(slot, "url(" + IMG + cfg.poster + ")");
        } else {
          var v = document.createElement("video");
          v.src = VID;
          v.autoplay = true;
          v.muted = true;
          v.loop = true;
          v.setAttribute("playsinline", "");
          v.setAttribute("aria-hidden", "true");
          v.poster = IMG + cfg.poster;
          v.style.cssText = "position:absolute;inset:0;width:100%;height:100%;object-fit:cover;";
          slot.style.position = slot.style.position || "relative";
          slot.style.overflow = "hidden";
          slot.appendChild(v);
        }
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", apply);
  } else {
    apply();
  }
})();
