# Copyright 2019 Akiomi Kamakura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL import Image, ImageChops

from pilgram import css
from pilgram import util


def rise(im):
    """Applies Rise filter.

    Arguments:
        im: An input image.

    Returns:
        The output image.
    """

    cb = util.or_convert(im, 'RGB')

    cs1 = util.fill(cb.size, [236, 205, 169])
    cm1 = ImageChops.multiply(cb, cs1)
    cm1 = Image.blend(cb, cm1, .15)

    cs2 = util.fill(cb.size, [50, 30, 7])
    cm2 = ImageChops.multiply(cb, cs2)
    cm2 = Image.blend(cb, cm2, .4)

    gradient_mask1 = util.radial_gradient_mask(cb.size, length=.55)
    cm = Image.composite(cm1, cm2, gradient_mask1)

    cs3 = util.fill(cb.size, [232, 197, 152])
    cm3 = css.blending.overlay(cm, cs3)
    cm3 = Image.blend(cm, cm3, .8)

    gradient_mask2 = util.radial_gradient_mask(cb.size, scale=.9)
    cm_ = Image.composite(cm3, cm, gradient_mask2)
    cr = Image.blend(cm, cm_, .6)

    cr = css.brightness(cr, 1.05)
    cr = css.sepia(cr, .2)
    cr = css.contrast(cr, .9)
    cr = css.saturate(cr, .9)

    return cr
