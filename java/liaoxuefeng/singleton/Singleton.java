public class Singleton{

    /**
     * 1. private 构造方法
     * 2. private static 持有唯一实例，全局唯一性
     * 3. public static 返回唯一实例
     * 
     * 延迟加载：
     *  在 private static 种不要直接 new，而是在调用 public static 时根据条件 new
     * 在多线程下是不安全的（不正确的）
     * 可以加锁解决
     * 
     * 加锁会严重影响并发性能
     * java 内存模型使得双重检查可能不成立
     * 
     * 使用 enum 实现 Singleton 的好处：
     * java 语法层面保证单利
     * 避免反序列化绕过普通类 private构造多个实例，反序列化后也是单利
     * 
     * 借助框架“约定”，一般不用刻意实现
     */ 
    

    // private static final Singleton Instance = new Singleton();

    // private Singleton(){
        
    // }

    // public static Singleton getInstance(){
    //     return Instance;
    // }

    private static final Singleton Instance = null;

    private Singleton(){}

    // public static Singleton getInstance(){
    //     if(Instance ==null){
    //         Instance = new Singleton();
    //     }
    //     return Instance;
    // }

    public synchronized static Singleton getInstance(){
        if(Instance ==null){
            Instance = new Singleton();
        }
        return Instance;
    }
}