# Wallpapers

A small, curated collection of atmospheric science-fiction and industrial-noir desktop wallpapers.

Everything listed below is committed under `wallpapers/`, so the images are available when the repo is consumed as a Git/Nix input. Sources and rights for third-party works are recorded in the tables, not in a separate index file.

## Included images

| File | Creator | Source | Rights | Size |
| --- | --- | --- | --- | --- |
| [`violet-monolith.png`](wallpapers/violet-monolith.png) | Generated for this collection | Original | Original, generated | 1672 × 941 |
| [`rainy-megacity.png`](wallpapers/rainy-megacity.png) | Generated for this collection | Original | Original, generated | 1672 × 941 |
| [`dystopian-dreams.png`](wallpapers/dystopian-dreams.png) | robokoboto | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1384548) | Personal use only | 4072 × 2280 |
| [`shattered-space.jpg`](wallpapers/shattered-space.jpg) | Bethesda Game Studios | [Official wallpaper](https://bethesda.net/en/game/starfield/media/wallpaper/starfield-shattered-space-wallpaper) | Publisher copyright | 5654 × 2763 |
| [`derelict-orbital-citadel.jpg`](wallpapers/derelict-orbital-citadel.jpg) | Paul Chadeisson | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1269192) | Personal use only | 3840 × 1632 |
| [`celestial-megaship.jpg`](wallpapers/celestial-megaship.jpg) | AI-generated / publisher Fred | [backiee](https://backiee.com/wallpaper/celestial-megaship-amidst-galactic-fog/302530) | Unverified | 1920 × 1080 |
| [`sci-fi-city.jpg`](wallpapers/sci-fi-city.jpg) | Annibale Siconolfi | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1108470) | Personal use only | 1920 × 1200 |
| [`futuristic-sci-fi-cityscape.jpg`](wallpapers/futuristic-sci-fi-cityscape.jpg) | Annibale Siconolfi | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1223603) | Personal use only | 5120 × 3200 |
| [`futuristic-space-colony.jpg`](wallpapers/futuristic-space-colony.jpg) | Paul Chadeisson | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=928392) | Personal use only | 1920 × 1102 |
| [`planet-among-stars.jpg`](wallpapers/planet-among-stars.jpg) | Unverified | [HDQ Walls](https://hdqwalls.com/planet-science-fiction-among-stars-4k-wallpaper) | Unverified | 3840 × 2160 |
| [`cosmic-pyramids.jpg`](wallpapers/cosmic-pyramids.jpg) | Unverified | [HDQ Walls](https://images.hdqwalls.com/download/cosmic-pyramids-ancient-future-yf-3840x2160.jpg) | Unverified | 3840 × 2160 |
| [`remember-me-slum-neoparis.jpg`](wallpapers/remember-me-slum-neoparis.jpg) | Paul Chadeisson | [ArtStation](https://www.artstation.com/artwork/zmx6) | Artist copyright | 1600 × 943 |
| [`museum-alien-life.jpg`](wallpapers/museum-alien-life.jpg) | Creator unverified | [Behance](https://www.behance.net/gallery/106183577/The-Museum-of-Alien-Life) | Unverified | 2800 × 1575 |

The two generated images are original concepts, not native 4K artwork. Bundled third-party files are kept at the largest resolution the source served, unmodified. Some sit below the source's advertised size: ArtStation only exposes 1600 px for the Remember Me piece, and backiee only serves 1920 × 1080. The Behance entry is a multi-image project; the bundled file is its cover image.

★ Initial favorites were Dystopian Dreams and Starfield: Shattered Space. The star is a preference, not a licensing designation.

## Use as a Nix flake input

In `repparw/nix/modules/aspects/style.nix`, add:

```nix
flake-file.inputs.wallpapers = {
  url = "github:repparw/wallpapers";
  flake = false;
};
```

The repo itself does **not** need a `flake.nix`. In the existing `stylix` `let` block, replace the current external `pkgs.fetchurl` image expression with:

```nix
inputImage = "${inputs.wallpapers}/wallpapers/violet-monolith.png";
```

Any file in the table above works the same way. Keep the existing `pkgs.runCommand` dimming pipeline and `stylix.image = wallpaper` configuration unchanged. Since the Nix repo uses `flake-file`, regenerate its `flake.nix` using the existing `write-flake` workflow, then update the lock file.

## Copyright and attribution

The two generated images carry no license yet. Every other file is third-party artwork redistributed here without permission: Wallpaper Abyss labels several works "Free For Private, Personal Use," which is not a grant to republish them, Bethesda's wallpaper is publisher copyright, and several creators are unverified. Attribution and source links are preserved above. ArtStation and Behance were fetched through a real browser session; that changed nothing about the rights.

Treat this repository as private until each work's terms are cleared or the files are replaced with original art. There is no blanket license for the collection.
