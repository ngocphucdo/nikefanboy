from model import Product, Category
from flask import *
import mlab
import cloudinary
from cloudinary import uploader
mlab.connect()
app = Flask(__name__)

cloudinary.config(
    cloud_name='nikefanboy',
    api_key="218223287849854",
    api_secret="etOBypj_IV0WiUXsKG2d89HvIkY"
)


@app.route('/')
def index():
    products = Product.objects.all()
    return render_template('index.html', products=products)


@app.route("/product/<id>")
def shoe_info(id):
    product = Product.objects.get(id=id)
    return render_template('product-detail.html', product=product)


@app.route("/category/<cate_name>")
def category(cate_name):
    products = Product.objects(cate_name=cate_name)
    return render_template('cate-info.html', products=products)


@app.route('/admin/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("admin-upload.html")
    else:
        file = request.files.getlist('image')[0]
        # upload image cloudinary
        img_cloud = uploader.upload(file)
        img_link = img_cloud['url']

        name = request.form['name']
        code = request.form['code']
        price = request.form['price']
        detail = request.form['detail']
        cate_name = request.form['cate_name']

        product = Product(image=img_link, name=name, code=code,
                          cate_name=cate_name, price=price, detail=detail)
        product.save()

        return redirect(url_for('index'))


@app.route('/admin/manage')
def manage():
    products = Product.objects()
    return render_template('admin-manage.html', all_products=products)


@app.route('/admin/delete/<id>')
def delete(id):
    product_to_delete = Product.objects().with_id(id)
    product_to_delete.delete()
    return redirect(url_for('index'))


@app.route('/admin/update/<id>', methods=['GET', 'POST'])
def update(id):
    updateProduct = Product.objects.get(id=id)
    products = Product.objects()
    if request.method == "GET":
        return render_template('update-product.html', updateProduct=updateProduct)
    elif request.method == "POST":
        form = request.form

        name = form['name']
        price = form['price']
        code = form['code']
        cate_name = form['cate_name']

        updateProduct.update(set__name=name, set__price=price,
                             set__code=code, set__cate_name=cate_name)
    return render_template('admin-manage.html', all_products=products)


if __name__ == '__main__':
    app.run(debug=True)
